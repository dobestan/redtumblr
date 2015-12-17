from hashids import Hashids


def _get_hashid_object(instance, min_length=6):
    return Hashids(salt=instance.__class__.__name__, min_length=min_length)


def get_encoded_hashid(instance, min_length=6):
    hashid = _get_hashid_object(instance, min_length=min_length)
    return hashid.encode(instance.id)
