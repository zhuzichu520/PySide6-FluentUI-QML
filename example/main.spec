# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all,collect_submodules

datas = [('./resource/example_rc.py', '.')]
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

excludes_binaries = ['PySide6\\Qt6Location.dll','PySide6\\Qt6WebChannel.dll',PySide6\\Qt6WebEngineQuick.dll','PySide6\\Qt6WebEngineQuickDelegatesQml.dll','PySide6\\Qt6WebSockets.dll','PySide6\\Qt6VirtualKeyboard.dll','PySide6\\Qt6PdfQuick.dll','PySide6\\Qt6Pdf.dll','PySide6\\Qt6QuickTimeline.dll','PySide6\\Qt6DataVisualizationQml.dll','PySide6\\Qt6DataVisualization.dll','PySide6\\Qt6Charts.dll','PySide6\\Qt6ChartsQml.dll','PySide6\\Qt6WebEngineCore.dll','PySide6\\Qt6Quick3D.dll','PySide6\\Qt6Quick3DAssetImport.dll','PySide6\\Qt6Quick3D.dll','PySide6\\Qt6Quick3DAssetUtils.dll','PySide6\\Qt6Quick3DEffects.dll','PySide6\\Qt6Quick3DHelpers.dll','PySide6\\Qt6Quick3DParticleEffects.dll','PySide6\\Qt6Quick3DParticles.dll','PySide6\\Qt6Quick3DRuntimeRender.dll','PySide6\\Qt6Quick3D.dll','PySide6\\Qt6Quick3DUtils.dll']
	
a.binaries = [x for x in a.binaries if x[0] not in excludes_binaries]

pyz = PYZ(a.pure)

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
	icon='./resource/res/image/favicon.ico'
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='example',
)