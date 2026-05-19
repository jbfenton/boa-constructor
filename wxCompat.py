# -*- coding: utf-8 -*-
# try:
#     from wx import NO_3D as wxNO_3D
# except ImportError:
#     from wx import wxNO_3D

try:
    from wx import DIALOG_MODAL as _wxDIALOG_MODAL
except ImportError:
    pass
else:
    wxDIALOG_MODAL = _wxDIALOG_MODAL

try:
    from wx import DIALOG_MODELESS as _wxDIALOG_MODELESS
except ImportError:
    pass
else:
    wxDIALOG_MODELESS = _wxDIALOG_MODELESS

try:
    from wx.tools.img2py import crunch_data as _crunch_data
except ImportError:
    pass
else:
    crunch_data = _crunch_data
