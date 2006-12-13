"""NVDA constants"""
#constants.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2006 Michael Curran <mick@kulgan.net>
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

#Core executer types
EXEC_SPEECH=0
EXEC_KEYBOARD=1
EXEC_MOUSE=2
EXEC_USERINTERFACE=3
EXEC_CONFIG=4
EXEC_LAST=4

#What to do with states
STATEACTION_IGNORE=0
STATEACTION_ON=1
STATEACTION_OFF=2

#IAccessible interface clsID
iid_IAccessible="{618736E0-3C3D-11CF-810C-00AA00389B71}"

#MSAA Object IDs
OBJID_WINDOW=0
OBJID_SYSMENU=-1
OBJID_TITLEBAR=-2
OBJID_MENU=-3
OBJID_CLIENT=-4
OBJID_VSCROLL=-5
OBJID_HSCROLL=-6
OBJID_SIZEGRIP=-7
OBJID_CARET=-8
OBJID_CURSOR=-9
OBJID_ALERT=-10
OBJID_SOUND=-11
OBJID_NATIVEOM=-16

#MSAA navigation
NAVDIR_DOWN=2
NAVDIR_FIRSTCHILD=7
NAVDIR_LASTCHILD=8
NAVDIR_LEFT=3
NAVDIR_NEXT=5
NAVDIR_PREVIOUS=6
NAVDIR_RIGHT=4
NAVDIR_UP=1

#win events
EVENT_SYSTEM_SOUND=0x1
EVENT_SYSTEM_ALERT=0x2
EVENT_SYSTEM_FOREGROUND=0x3
EVENT_SYSTEM_MENUSTART=0x4
EVENT_SYSTEM_MENUEND=0x5
EVENT_SYSTEM_MENUPOPUPSTART=0x6
EVENT_SYSTEM_MENUPOPUPEND=0x7
EVENT_SYSTEM_CAPTURESTART=0x8
EVENT_SYSTEM_CAPTUREEND=0x9
EVENT_SYSTEM_MOVESIZESTART=0xa
EVENT_SYSTEM_MOVESIZEEND=0xb
EVENT_SYSTEM_CONTEXTHELPSTART=0xc
EVENT_SYSTEM_CONTEXTHELPEND=0xd
EVENT_SYSTEM_DRAGDROPSTART=0xe
EVENT_SYSTEM_DRAGDROPEND=0xf
EVENT_SYSTEM_DIALOGSTART=0x10
EVENT_SYSTEM_DIALOGEND=0x11
EVENT_SYSTEM_SCROLLINGSTART=0x12
EVENT_SYSTEM_SCROLLINGEND=0x13
EVENT_SYSTEM_SWITCHSTART=0x14
EVENT_SYSTEM_SWITCHEND=0x15
EVENT_SYSTEM_MINIMIZESTART=0x16
EVENT_SYSTEM_MINIMIZEEND=0x17
EVENT_OBJECT_CREATE=0x8000
EVENT_OBJECT_DESTROY=0x8001
EVENT_OBJECT_SHOW=0x8002
EVENT_OBJECT_HIDE=0x8003
EVENT_OBJECT_REORDER=0x8004
EVENT_OBJECT_FOCUS=0x8005
EVENT_OBJECT_SELECTION=0x8006
EVENT_OBJECT_SELECTIONADD=0x8007
EVENT_OBJECT_SELECTIONREMOVE=0x8008
EVENT_OBJECT_SELECTIONWITHIN=0x8009
EVENT_OBJECT_STATECHANGE=0x800a
EVENT_OBJECT_LOCATIONCHANGE=0x800b
EVENT_OBJECT_NAMECHANGE=0x800c
EVENT_OBJECT_DESCRIPTIONCHANGE=0x800d
EVENT_OBJECT_VALUECHANGE=0x800e
EVENT_OBJECT_PARENTCHANGE=0x800f
EVENT_OBJECT_HELPCHANGE=0x8010
EVENT_OBJECT_DEFACTIONCHANGE=0x8011
EVENT_OBJECT_ACCELERATORCHANGE=0x8012
EVENT_CONSOLE_CARET=0x4001
EVENT_CONSOLE_UPDATE_REGION=0x4002
EVENT_CONSOLE_UPDATE_SIMPLE=0x4003
EVENT_CONSOLE_UPDATE_SCROLL=0x4004
EVENT_CONSOLE_LAYOUT=0x4005

#MSAA roles
ROLE_SYSTEM_ALERT=8
ROLE_SYSTEM_ANIMATION=54
ROLE_SYSTEM_APPLICATION=14
ROLE_SYSTEM_BORDER=19
ROLE_SYSTEM_BUTTONDROPDOWN=56
ROLE_SYSTEM_BUTTONDROPDOWNGRID=58
ROLE_SYSTEM_BUTTONMENU=57
ROLE_SYSTEM_CARET=7
ROLE_SYSTEM_CELL=29
ROLE_SYSTEM_CHARACTER=32
ROLE_SYSTEM_CHART=17
ROLE_SYSTEM_CHECKBUTTON=44
ROLE_SYSTEM_CLIENT=10
ROLE_SYSTEM_CLOCK=61
ROLE_SYSTEM_COLUMN=27
ROLE_SYSTEM_COLUMNHEADER=25
ROLE_SYSTEM_COMBOBOX=46
ROLE_SYSTEM_CURSOR=6
ROLE_SYSTEM_DIAGRAM=53
ROLE_SYSTEM_DIAL=49
ROLE_SYSTEM_DIALOG=18
ROLE_SYSTEM_DOCUMENT=15
ROLE_SYSTEM_DROPLIST=47
ROLE_SYSTEM_EQUATION=55
ROLE_SYSTEM_GRAPHIC=40
ROLE_SYSTEM_GRIP=4
ROLE_SYSTEM_GROUPING=20
ROLE_SYSTEM_HELPBALLOON=31
ROLE_SYSTEM_HOTKEYFIELD=50
ROLE_SYSTEM_INDICATOR=39
ROLE_SYSTEM_LINK=30
ROLE_SYSTEM_LIST=33
ROLE_SYSTEM_LISTITEM=34
ROLE_SYSTEM_MENUBAR=2
ROLE_SYSTEM_MENUITEM=12
ROLE_SYSTEM_MENUPOPUP=11
ROLE_SYSTEM_OUTLINE=35
ROLE_SYSTEM_OUTLINEITEM=36
ROLE_SYSTEM_PAGETAB=37
ROLE_SYSTEM_PAGETABLIST=60
ROLE_SYSTEM_PANE=16
ROLE_SYSTEM_PROGRESSBAR=48
ROLE_SYSTEM_PROPERTYPAGE=38
ROLE_SYSTEM_PUSHBUTTON=43
ROLE_SYSTEM_RADIOBUTTON=45
ROLE_SYSTEM_ROW=28
ROLE_SYSTEM_ROWHEADER=26
ROLE_SYSTEM_SCROLLBAR=3
ROLE_SYSTEM_SEPARATOR=21
ROLE_SYSTEM_SLIDER=51
ROLE_SYSTEM_SOUND=5
ROLE_SYSTEM_SPINBUTTON=52
ROLE_SYSTEM_STATICTEXT=41
ROLE_SYSTEM_STATUSBAR=23
ROLE_SYSTEM_TABLE=24
ROLE_SYSTEM_TEXT=42
ROLE_SYSTEM_TITLEBAR=1
ROLE_SYSTEM_TOOLBAR=22
ROLE_SYSTEM_TOOLTIP=13
ROLE_SYSTEM_WHITESPACE=59
ROLE_SYSTEM_WINDOW=9
ROLE_SYSTEM_SPLITBUTTON=62
ROLE_SYSTEM_OUTLINEBUTTON=64

#MSAA states
STATE_SYSTEM_UNAVAILABLE=0x1
STATE_SYSTEM_SELECTED=0x2
STATE_SYSTEM_FOCUSED=0x4
STATE_SYSTEM_PRESSED=0x8
STATE_SYSTEM_CHECKED=0x10
STATE_SYSTEM_MIXED=0x20
STATE_SYSTEM_READONLY=0x40
STATE_SYSTEM_HOTTRACKED=0x80
STATE_SYSTEM_DEFAULT=0x100
STATE_SYSTEM_EXPANDED=0x200
STATE_SYSTEM_COLLAPSED=0x400
STATE_SYSTEM_BUSY=0x800
STATE_SYSTEM_FLOATING=0x1000
STATE_SYSTEM_MARQUEED=0x2000
STATE_SYSTEM_ANIMATED=0x4000
STATE_SYSTEM_INVISIBLE=0x8000
STATE_SYSTEM_OFFSCREEN=0x10000
STATE_SYSTEM_SIZEABLE=0x20000
STATE_SYSTEM_MOVEABLE=0x40000
STATE_SYSTEM_SELFVOICING=0x80000
STATE_SYSTEM_FOCUSABLE=0x100000
STATE_SYSTEM_SELECTABLE=0x200000
STATE_SYSTEM_LINKED=0x400000
STATE_SYSTEM_TRAVERSED=0x800000
STATE_SYSTEM_MULTISELECTABLE=0x1000000
STATE_SYSTEM_EXTSELECTABLE=0x2000000
STATE_SYSTEM_HASSUBMENU=0x4000000
STATE_SYSTEM_ALERT_LOW=0x4000000
STATE_SYSTEM_ALERT_MEDIUM=0x8000000
STATE_SYSTEM_ALERT_HIGH=0x10000000
STATE_SYSTEM_PROTECTED=0x20000000
STATE_SYSTEM_HASPOPUP=0x40000000
STATE_SYSTEM_VALID=0x1fffffff

#Windows hooks
WH_KEYBOARD=2
WH_MOUSE=7

#Keys
VK_LBUTTON=1
VK_RBUTTON=2
VK_CANCEL=3
VK_MBUTTON=4
VK_XBUTTON=15
VK_XBUTTON=26
VK_BACK=8
VK_TAB=9
VK_CLEAR=12
VK_RETURN=13
VK_SHIFT=16
VK_CONTROL=17
VK_MENU=18
VK_PAUSE=19
VK_CAPITAL=20
VK_FINAL=0x18
VK_ESCAPE=0x1B
VK_CONVERT=0x1C
VK_NONCONVERT=0x1D
VK_ACCEPT=0x1E
VK_MODECHANGE=0x1F
VK_SPACE=32
VK_PRIOR=33
VK_NEXT=34
VK_END=35
VK_HOME=36
VK_LEFT=37
VK_UP=38
VK_RIGHT=39
VK_DOWN=40
VK_SELECT=41
VK_PRINT=42
VK_EXECUTE=43
VK_SNAPSHOT=44
VK_INSERT=45
VK_DELETE=46
VK_HELP=47
VK_LWIN=0x5B
VK_RWIN=0x5C
VK_APPS=0x5D
VK_SLEEP=0x5F
VK_NUMPAD0=0x60
VK_NUMPAD1=0x61
VK_NUMPAD2=0x62
VK_NUMPAD3=0x63
VK_NUMPAD4=0x64
VK_NUMPAD5=0x65
VK_NUMPAD6=0x66
VK_NUMPAD7=0x67
VK_NUMPAD8=0x68
VK_NUMPAD9=0x69
VK_MULTIPLY=0x6A
VK_ADD=0x6B
VK_SEPARATOR=0x6C
VK_SUBTRACT=0x6D
VK_DECIMAL=0x6E
VK_DIVIDE=0x6F
VK_F1=0x70
VK_F2=0x71
VK_F3=0x72
VK_F4=0x73
VK_F5=0x74
VK_F6=0x75
VK_F7=0x76
VK_F8=0x77
VK_F9=0x78
VK_F10=0x79
VK_F11=0x7A
VK_F12=0x7B
VK_F13=0x7C
VK_F14=0x7D
VK_F15=0x7E
VK_F16=0x7F
VK_F17=0x80
VK_F18=0x81
VK_F19=0x82
VK_F20=0x83
VK_F21=0x84
VK_F22=0x85
VK_F23=0x86
VK_F24=0x87
VK_NUMLOCK=0x90
VK_SCROLL=0x91
VK_LSHIFT=0xA0
VK_RSHIFT=0xA1
VK_LCONTROL=0xA2
VK_RCONTROL=0xA3
VK_LMENU=0xA4
VK_RMENU=0xA5

#Window messages
WM_GETTEXT=13
WM_GETTEXTLENGTH=14
EM_GETSEL=176
EM_SETSEL=177
EM_GETLINE=196
EM_GETLINECOUNT=186
EM_LINEFROMCHAR=201
EM_LINEINDEX=187
EM_LINELENGTH=193
EM_POSFROMCHAR=214 
EM_CHARFROMPOS=215
 

#Window console
STD_INPUT_HANDLE=-10
STD_OUTPUT_HANDLE=-11
STD_ERROR_HANDLE=-12

#Processes
PROCESS_ALL_ACCESS=0x1F0FFF
READ_CONTROL=0x20000

#getAncestor winuser function
GA_PARENT=1
GA_ROOT=2
GA_ROOTOWNER=3


