# a trivial example which uses a cython memoryview
cpdef test():
    cdef int carr[3]
    cdef int [:] carr_view = carr
    carr_view[:] = 42
