from triton  import ARCH
from pintool import *

Triton = getTritonContext()

def freeEntry(threadId):
    print('[!] free() found')

def mallocEntry(threadId):
    print('[!] malloc() found')

def memcpyEntry(threadId):
    print('[!] memcpy() found')

def strcpyEntry(threadId):
    print('[!] strcpy() found')

def strncpyEntry(threadId):
    print('[!] strncpy() found')

def printfEntry(threadId):
    print('[!] printf() found')

def putsEntry(threadId):
    print('[!] puts() found')

if __name__ == '__main__':
    # Start the symbolic analysis from the Entry point
    startAnalysisFromEntry()

    # Add callbacks
    insertCall(   freeEntry, INSERT_POINT.ROUTINE_ENTRY, "free")
    insertCall( mallocEntry, INSERT_POINT.ROUTINE_ENTRY, "malloc")
    insertCall( memcpyEntry, INSERT_POINT.ROUTINE_ENTRY, "memcpy")
    insertCall( strcpyEntry, INSERT_POINT.ROUTINE_ENTRY, "strcpy")
    insertCall(strncpyEntry, INSERT_POINT.ROUTINE_ENTRY, "strncpy")
    insertCall(   putsEntry, INSERT_POINT.ROUTINE_ENTRY, "puts")
    insertCall( printfEntry, INSERT_POINT.ROUTINE_ENTRY, "printf")

    # Run the instrumentation - Never returns
    runProgram()
