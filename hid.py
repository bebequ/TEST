import os
import ctypes

lib_names = ["hidapi.dll", "hidapi.so", "hidapi.dylib"]
for lib_name in lib_names:
    try:
        print(os.path.join(os.getcwd(), lib_name))
        hidapi = ctypes.cdll.LoadLibrary(os.path.join(os.getcwd(),lib_name))
        break
    except OSError:
        pass
else:
    error = "Unable to load any of the following libraries: {}".format(" "\
            .join(lib_names))
    raise ImportError(error)

class DeviceInfo(ctypes.Structure):
	def as_dict(self):
		ret = {}
		for name, type in self._fields_:
			if name == 'next':
				continue
			ret[name] = getattr(self, name, None)
DeviceInfo._fields_ = [
	('path', ctypes.c_char_p),
	('vendor_id', ctypes.c_ushort),
	('product_id', ctypes.c_ushort),
	('serial_number', ctypes.c_wchar_p),
	('release_number', ctypes.c_ushort),
	('manufacturer_string', ctypes.c_ushort),
	('product_string', ctypes.c_wchar_p),
	('usage_page', ctypes.c_ushort),
	('usage', ctypes.c_ushort),
	('interface_number', ctypes.c_int),
	('next', ctypes.POINTER(DeviceInfo)),
]

hidapi.hid_init()
#hidapi.hid_close()

hidapi.hid_init.argtypes = []
hidapi.hid_init.restype = ctypes.c_int
hidapi.hid_exit.argtypes = []
hidapi.hid_exit.restype = ctypes.c_int
hidapi.hid_enumerate.argtypes = [ctypes.c_ushort, ctypes.c_ushort]
hidapi.hid_enumerate.restype = ctypes.POINTER(DeviceInfo)
hidapi.hid_free_enumeration.argtypes = [ctypes.POINTER(DeviceInfo)]
hidapi.hid_free_enumeration.restype = None
hidapi.hid_open.argtypes = [ctypes.c_ushort, ctypes.c_ushort, ctypes.c_int, ctypes.c_wchar_p]
hidapi.hid_open.restype = ctypes.c_void_p
hidapi.hid_open_path.argtypes = [ctypes.c_char_p]
hidapi.hid_open_path.restype = ctypes.c_void_p
hidapi.hid_write.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
hidapi.hid_write.restype = ctypes.c_int
hidapi.hid_read_timeout.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t, ctypes.c_int]
hidapi.hid_read_timeout.restype = ctypes.c_int
hidapi.hid_read.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
hidapi.hid_read.restype = ctypes.c_int
hidapi.hid_set_nonblocking.argtypes = [ctypes.c_void_p, ctypes.c_int]
hidapi.hid_set_nonblocking.restype = ctypes.c_int
hidapi.hid_send_feature_report.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
hidapi.hid_send_feature_report.restype = ctypes.c_int
hidapi.hid_get_feature_report.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t]
hidapi.hid_get_feature_report.restype = ctypes.c_int
hidapi.hid_close.argtypes = [ctypes.c_void_p]
hidapi.hid_close.restype = None
hidapi.hid_get_manufacturer_string.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_size_t]
hidapi.hid_get_manufacturer_string.restype = ctypes.c_int
hidapi.hid_get_product_string.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_size_t]
hidapi.hid_get_product_string.restype = ctypes.c_int
hidapi.hid_get_serial_number_string.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_size_t]
hidapi.hid_get_serial_number_string.restype = ctypes.c_int
hidapi.hid_get_indexed_string.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_wchar_p, ctypes.c_size_t]
hidapi.hid_get_indexed_string.restype = ctypes.c_int
hidapi.hid_error.argtypes = [ctypes.c_void_p]
hidapi.hid_error.restype = ctypes.c_wchar_p
