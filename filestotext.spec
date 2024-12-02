# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Define version here since we can't import it from the main script
VERSION = "0.1"

a = Analysis(
    ['filestotext.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets',
        'PyQt5.sip'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='filestotext',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=True,
    target_arch='arm64',
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='filestotext',
)

app = BUNDLE(
    coll,
    name='filestotext.app',
    icon=None,
    bundle_identifier='com.filestotext.app',
    info_plist={
        'LSMinimumSystemVersion': '11.0',
        'NSHighResolutionCapable': True,
        'NSRequiresAquaSystemAppearance': False,
        'CFBundleShortVersionString': VERSION,
        'NSPrincipalClass': 'NSApplication',
        'CFBundleDocumentTypes': [],
        'CFBundleSupportedPlatforms': ['MacOSX'],
        'LSApplicationCategoryType': 'public.app-category.utilities',
    },
)
