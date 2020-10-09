from django.core.exceptions import ObjectDoesNotExist

from .ChildType import ChildType
from ..models.model.DealerLocation import DealerLocation


class ExternalAttributeTerm(object):
    pass


get_types = {ChildType.DEALER_LOCATION: DealerLocation,
             }

update_types = {ChildType.DEALER_LOCATION: lambda i, d: DealerLocation.objects.create(dealer=i, **d),
                }


def update_item(instance, data_list, item_type: ChildType):
    item_type_class = get_types.get(item_type)
    lambda_update_function = update_types.get(item_type)
    print(data_list)
    for i in range(len(data_list)):
        data_item = data_list[i]
        print(data_item)
        '''
        As it is not possible to say that the absence is an indication of deletion for child objects
        they are marked for purge. This is picked up and the object deleted from the database. If the 
        object can not be found no error processing takes place as could be a new object added then marked
        for purge without it being saved to the database.
        '''
        if data_item.get('purge') is True:
            try:
                delete_item = item_type_class.objects.get(pk=data_item.get('itemIdentifier'))
            #               delete_item.delete()
            except ObjectDoesNotExist:
                pass
        else:
            '''
            Updating of the child will look to extract the child from the database, if this is not possible 
            as the child maybe new then it is created and stored in the database. If this is an update the 
            field and value are taken from the dict and used to set the attribute of the retrieved object.
            '''
            try:
                item_instance = item_type_class.objects.get(pk=data_item.get('itemIdentifier'))
            #                for field, value in data_item.items():
            #                   setattr(item_instance, field, value)
            #                item_instance.save()
            except ObjectDoesNotExist:
               item_instance = lambda_update_function(instance, data_item)  #
               item_instance.save()
