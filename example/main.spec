# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_all,collect_submodules

datas = [('./resource/example_rc.py', '.')]
if os.path.exists('./example/version.py'):
    datas.append(('./version.py', '.'))
binaries = []
hiddenimports = []
excludedimports = []
tmp_ret = collect_all('FluentUI')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
	excludedimports=excludedimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

excludes_binaries = [
    'Qt6Location.dll',
    'Qt6WebChannel.dll',
    'Qt6WebEngineQuick.dll',
    'Qt6WebEngineQuickDelegatesQml.dll',
    'Qt6WebSockets.dll',
    'Qt6VirtualKeyboard.dll',
    'Qt6PdfQuick.dll',
    'Qt6Pdf.dll',
    'Qt6QuickTimeline.dll',
    'Qt6DataVisualizationQml.dll',
    'Qt6DataVisualization.dll',
    'Qt6Charts.dll',
    'Qt6ChartsQml.dll',
    'Qt6WebEngineCore.dll',
    'Qt6Quick3D.dll',
    'Qt6Quick3DAssetImport.dll',
    'Qt6Quick3D.dll',
    'Qt6Quick3DAssetUtils.dll',
    'Qt6Quick3DEffects.dll',
    'Qt6Quick3DHelpers.dll',
    'Qt6Quick3DParticleEffects.dll',
    'Qt6Quick3DParticles.dll',
    'Qt6Quick3DRuntimeRender.dll',
    'Qt6Quick3D.dll',
    'Qt6Quick3DUtils.dll'
    ]

a.binaries = [x for x in a.binaries if os.path.basename(x[0]) not in excludes_binaries]

pyz = PYZ(a.pure)

file_version = None
file_version_name = "action-cli/file_version_info.txt"
current_directory = os.getcwd()
file_version_path = os.path.join(current_directory, file_version_name)
if os.path.exists(file_version_path):
    file_version = './../action-cli/file_version_info.txt'
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='example',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
	icon='./resource/res/image/favicon.ico',
    version=file_version
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='',
)