AR = 'arm-none-eabi-ar'
ARFLAGS = 'rcs'
AS = 'arm-none-eabi-gcc'
BINDIR = '/usr/local/bin'
BLOCK_MESSAGE_KEYS = []
BUILD_DIR = 'aplite'
BUILD_TYPE = 'app'
BUNDLE_BIN_DIR = 'aplite'
BUNDLE_NAME = 'pogo_assistant 2.pbw'
CC = ['arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '7', '2')
CFLAGS = ['-std=c99', '-mcpu=cortex-m3', '-mthumb', '-ffunction-sections', '-fdata-sections', '-g', '-fPIE', '-Os', '-D_TIME_H_', '-Wall', '-Wextra', '-Werror', '-Wno-unused-parameter', '-Wno-error=unused-function', '-Wno-error=unused-variable']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CPPPATH_ST = '-I%s'
DEFINES = ['RELEASE', 'PBL_PLATFORM_APLITE', 'PBL_BW', 'PBL_RECT', 'PBL_SDK_3']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'darwin'
INCLUDES = ['aplite']
LD = 'arm-none-eabi-ld'
LIBDIR = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_DIR = 'node_modules'
LIB_ST = '-l%s'
LINKFLAGS = ['-mcpu=cortex-m3', '-mthumb', '-Wl,--gc-sections', '-Wl,--warn-common', '-fPIE', '-Os']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINK_CC = ['arm-none-eabi-gcc']
MESSAGE_KEYS = {u'status': 0, u'typetwo': 3, u'defense': 8, u'name': 6, u'fleerate': 5, u'stamina': 7, u'attack': 9, u'typeone': 2, u'caprate': 4, u'message': 1, u'angle': 10}
MESSAGE_KEYS_DEFINITION = '/Users/Liam/pebble-dev/pogo_assistant 2/build/src/message_keys.auto.c'
MESSAGE_KEYS_HEADER = '/Users/Liam/pebble-dev/pogo_assistant 2/build/include/message_keys.auto.h'
MESSAGE_KEYS_JSON = '/Users/Liam/pebble-dev/pogo_assistant 2/build/js/message_keys.json'
PEBBLE_SDK_COMMON = '/Users/Liam/Library/Application Support/Pebble SDK/SDKs/current/sdk-core/pebble/common'
PEBBLE_SDK_PLATFORM = '/Users/Liam/Library/Application Support/Pebble SDK/SDKs/current/sdk-core/pebble/aplite'
PEBBLE_SDK_ROOT = '/Users/Liam/Library/Application Support/Pebble SDK/SDKs/current/sdk-core/pebble'
PLATFORM = {'TAGS': ['aplite', 'bw', 'rect'], 'ADDITIONAL_TEXT_LINES_FOR_PEBBLE_H': [], 'MAX_APP_BINARY_SIZE': 65536, 'MAX_RESOURCES_SIZE': 524288, 'MAX_APP_MEMORY_SIZE': 24576, 'MAX_WORKER_MEMORY_SIZE': 10240, 'NAME': 'aplite', 'BUNDLE_BIN_DIR': 'aplite', 'BUILD_DIR': 'aplite', 'MAX_RESOURCES_SIZE_APPSTORE_2_X': 98304, 'MAX_RESOURCES_SIZE_APPSTORE': 131072, 'DEFINES': ['PBL_PLATFORM_APLITE', 'PBL_BW', 'PBL_RECT']}
PLATFORM_NAME = 'aplite'
PREFIX = '/usr/local'
PROJECT_INFO = {'appKeys': {u'status': 0, u'typetwo': 3, u'defense': 8, u'name': 6, u'fleerate': 5, u'stamina': 7, u'attack': 9, u'typeone': 2, u'caprate': 4, u'message': 1, u'angle': 10}, u'sdkVersion': u'3', u'projectType': u'native', u'uuid': u'3a0c00f6-e988-451f-85a0-3642ac363476', u'messageKeys': {u'status': 0, u'typetwo': 3, u'defense': 8, u'name': 6, u'fleerate': 5, u'stamina': 7, u'attack': 9, u'typeone': 2, u'caprate': 4, u'message': 1, u'angle': 10}, 'companyName': u'liam@mcmains.net', u'enableMultiJS': True, u'watchapp': {u'watchface': False}, u'capabilities': [u''], u'platforms': [u'basalt', u'aplite'], 'versionLabel': u'1.2', 'longName': u'PoGo Assistant', u'displayName': u'PoGo Assistant', 'shortName': u'PoGo Assistant', u'resources': {u'media': [{u'type': u'bitmap', u'menuIcon': False, u'targetPlatforms': None, u'name': u'UNABLE', u'file': u'images/unable.png'}, {u'type': u'bitmap', u'menuIcon': False, u'targetPlatforms': None, u'name': u'ARROW', u'file': u'images/arrow.png'}, {u'targetPlatforms': None, u'type': u'font', u'name': u'CODE_34', u'file': u'fonts/code.otf'}]}, 'name': u'pogo-assistant'}
REQUESTED_PLATFORMS = []
RESOURCES_JSON = [{u'type': u'bitmap', u'menuIcon': False, u'targetPlatforms': None, u'name': u'UNABLE', u'file': u'images/unable.png'}, {u'type': u'bitmap', u'menuIcon': False, u'targetPlatforms': None, u'name': u'ARROW', u'file': u'images/arrow.png'}, {u'targetPlatforms': None, u'type': u'font', u'name': u'CODE_34', u'file': u'fonts/code.otf'}]
RPATH_ST = '-Wl,-rpath,%s'
SDK_VERSION_MAJOR = 5
SDK_VERSION_MINOR = 78
SHLIB_MARKER = None
SIZE = 'arm-none-eabi-size'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = None
STLIB_ST = '-l%s'
SUPPORTED_PLATFORMS = ['aplite', 'basalt', 'chalk']
TARGET_PLATFORMS = ['chalk', 'basalt', 'aplite']
TIMESTAMP = 1469573718
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
macbundle_PATTERN = '%s.bundle'
