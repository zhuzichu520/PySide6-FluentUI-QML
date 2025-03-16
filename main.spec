import os
import sys

import env

mainPath = os.path.join('.', env.projectName, 'main.py')

a = Analysis(
    [mainPath],
    pathex=[],
    binaries=[],
    datas=[('./source.zip', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

if sys.platform.startswith("darwin"):
    excludes_binaries = [
        'QtLocation',
        'QtWebChannel',
        'QtWebEngineQuick',
        'QtWebEngineQuickDelegatesQml',
        'QtWebSockets',
        'QtVirtualKeyboard',
        'QtPdfQuick',
        'QtPdf',
        'QtQuickTimeline',
        'QtDataVisualizationQml',
        'QtDataVisualization',
        'QtCharts',
        'QtChartsQml',
        'QtWebEngineCore',
        'QtQuick3D',
        'QtQuick3DAssetImport',
        'QtQuick3D',
        'QtQuick3DAssetUtils',
        'QtQuick3DEffects',
        'QtQuick3DHelpers',
        'QtQuick3DParticleEffects',
        'QtQuick3DParticles',
        'QtQuick3DRuntimeRender',
        'QtQuick3D',
        'QtQuick3DUtils'
    ]
else:
    excludes_binaries = [
        'Qt6Location',
        'Qt6WebChannel',
        'Qt6WebEngineQuick',
        'Qt6WebEngineQuickDelegatesQml',
        'Qt6WebSockets',
        'Qt6VirtualKeyboard',
        'Qt6PdfQuick',
        'Qt6Pdf',
        'Qt6QuickTimeline',
        'Qt6DataVisualizationQml',
        'Qt6DataVisualization',
        'Qt6Charts',
        'Qt6ChartsQml',
        'Qt6WebEngineCore',
        'Qt6Quick3D',
        'Qt6Quick3DAssetImport',
        'Qt6Quick3D',
        'Qt6Quick3DAssetUtils',
        'Qt6Quick3DEffects',
        'Qt6Quick3DHelpers',
        'Qt6Quick3DParticleEffects',
        'Qt6Quick3DParticles',
        'Qt6Quick3DRuntimeRender',
        'Qt6Quick3D',
        'Qt6Quick3DUtils'
    ]

a.binaries = [x for x in a.binaries if not any(item in os.path.basename(x[0]) for item in excludes_binaries)]

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=env.projectName,
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
    icon='./favicon.ico'
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

app = BUNDLE(
    coll,
    name=env.projectName + '.app',
    icon='./favicon.icns',
    bundle_identifier=None
)
