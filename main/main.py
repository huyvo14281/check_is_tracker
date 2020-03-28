
from sqlalchemy import desc
from sqlalchemy.orm import Session

import config.database
import config.dns_lookup
from model.black_list import BlackList
from model.cname import Cname
import check_is_tracker

if __name__ == '__main__':
    master_session: Session = config.database.connect_master_session()
    replica_session: Session = config.database.connect_replica_session()

    block_objs = replica_session.query(BlackList).all()
    cname_objs = replica_session.query(Cname).all()

    replica_session.close()

    cname_obj: Cname
    block_obj: BlackList

    i = 0
    for cname_obj in cname_objs:
        cname_obj.update_is_tracker(is_tracker=0)
        for block_obj in block_objs:
            if check_is_tracker.is_tracker(domain=cname_obj.cname, block_domain=block_obj.domain) is True:
                cname_obj.update_is_tracker(is_tracker=1)
                break
        
        master_session.add(cname_obj)
        
        if i % 100 == 0:
            master_session.commit()
        
        i = i + 1
    master_session.close()
