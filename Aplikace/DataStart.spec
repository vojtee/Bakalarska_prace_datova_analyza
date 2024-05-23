# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['.venv/Lib/site-packages'],
    binaries=[],
    datas=[
        ('resources', 'resources'),
        ('.venv/Lib/site-packages/tkinterweb', 'tkinterweb'),
        ('.venv/Lib/site-packages/PIL', 'PIL')
    ],
    hiddenimports=[
        'PIL._imaging', 
        'tkinter', 
        'tkinterweb', 
        'geopy',
        'shapely',
        'pandas',
        'seaborn',
        'numpy',
        'matplotlib',
        'sklearn'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='DataStart',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
