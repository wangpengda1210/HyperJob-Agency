def unpack(input_tuple):
    # your code here
    assert isinstance(input_tuple, tuple)
    unpacked = ()
    for instance in input_tuple:
        if isinstance(instance, tuple):
            unpacked += instance
        else:
            unpacked += (instance,)
    return unpacked
