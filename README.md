# Libc Test

The purpose of this test is to check which symbols of libc functions can be
found and which can not.

## Sample
The sample binary file was compiled as follows:
```
gcc -g -o sample.elf sample.c -Wall -Wextra -O0
```

It contains following symbols, symbols which were not successfully hooked are marked.
```
~/libc_test$ nm -u sample.elf
                 U free@@GLIBC_2.2.5
                 U malloc@@GLIBC_2.2.5
                 U memcpy@@GLIBC_2.14         NOT FOUND
                 U printf@@GLIBC_2.2.5
                 U puts@@GLIBC_2.2.5
                 U strlen@@GLIBC_2.2.5
                 U strncpy@@GLIBC_2.2.5       NOT FOUND
```



## Test Run
```
~/libc_test$ sudo ../triton ./libc_test.py ./sample.elf 
[!] malloc() found
[!] strlen() found
[!] puts() found
[!] strlen() found
[!] malloc() found
Hallo
[!] printf() found
1
[!] free() found
```
