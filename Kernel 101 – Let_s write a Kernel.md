Kernel 101 – Let's write a Kernel

1.

### [Kernel 101 – Let’s write a Kernel](http://arjunsreedharan.org/post/82710718100/kernel-101-lets-write-a-kernel)

###### [Arjun Sreedharan](http://arjunsreedharan.org/)

Hello World,

Let us write a simple kernel which could be loaded with the GRUB bootloader on an x86 system. This kernel will display a message on the screen and then hang.

![One does simply write a kernel](../_resources/776cb363d518314f115ff40eea4bb981.jpg)

**How does an x86 machine boot**

Before we think about writing a kernel, let’s see how the machine boots up and transfers control to the kernel:

Most registers of the x86 CPU have well defined values after power-on. The Instruction Pointer (EIP) register holds the memory address for the instruction being executed by the processor. EIP is hardcoded to the value **0xFFFFFFF0**. Thus, the x86 CPU is hardwired to begin execution at the physical address 0xFFFFFFF0. It is in fact, the last 16 bytes of the 32-bit address space. This memory address is called reset vector.

Now, the chipset’s memory map makes sure that 0xFFFFFFF0 is mapped to a certain part of the BIOS, not to the RAM. Meanwhile, the BIOS copies itself to the RAM for faster access. This is called **shadowing**. The address 0xFFFFFFF0 will contain just a jump instruction to the address in memory where BIOS has copied itself.

Thus, the BIOS code starts its execution.  BIOS first searches for a bootable device in the configured boot device order. It checks for a certain magic number to determine if the device is bootable or not. (whether bytes 511 and 512 of first sector are **0xAA55**)

Once the BIOS has found a bootable device, it copies the contents of the device’s first sector into RAM starting from physical address **0x7c00**; and then jumps into the address and executes the code just loaded. This code is called the **bootloader**.

The bootloader then loads the kernel at the physical address **0x100000**. The address 0x100000 is used as the start-address for all big kernels on x86 machines.

All x86 processors begin in a simplistic 16-bit mode called **real mode**. The GRUB bootloader makes the switch to 32-bit **protected mode** by setting the lowest bit of [object Object] register to **1**. Thus the kernel loads in 32-bit protected mode.

Do note that in case of linux kernel, GRUB detects linux boot protocol and loads linux kernel in real mode. Linux kernel itself [makes the switch](http://github.com/torvalds/linux/blob/master/arch/x86/boot/main.c#L181) to protected mode.

**What all do we need?**
* An x86 computer (of course)
* Linux
* [NASM assembler](http://www.nasm.us/)
* gcc
* ld (GNU Linker)
* grub

**Source Code**

Source code is available at my [Github repository - mkernel](http://github.com/arjun024/mkernel)

**The entry point using assembly**

We like to write everything in C, but we cannot avoid a little bit of assembly. We will write a small file in x86 assembly-language that serves as the starting point for our kernel. All our assembly file will do is invoke an external function which we will write in C, and then halt the program flow.

How do we make sure that this assembly code will serve as the starting point of the kernel?

We will use a linker script that links the object files to produce the final kernel executable. (more explained later)  In this linker script, we will explicitly specify that we want our binary to be loaded at the address 0x100000. This address, as I have said earlier, is where the kernel is expected to be. Thus, the bootloader will take care of firing the kernel’s entry point.

Here’s the assembly code:
;;kernel.asmbits 32;nasm directive -  32 bit
section .textglobal startextern kmain ;kmain is  defined  in the c file
start: cli;block interrupts
mov esp, stack_space;set stack pointer
call kmain
hlt;halt the CPU
section .bss
resb 8192;8KB  for stack
stack_space:

The first instruction [object Object] is not an x86 assembly instruction. It’s a directive to the NASM assembler that specifies it should generate code to run on a processor operating in 32 bit mode. It is not mandatorily required in our example, however is included here as it’s good practice to be explicit.

The second line begins the text section (aka code section). This is where we put all our code.

[object Object] is another NASM directive to set symbols from source code as global. By doing so, the linker knows where the symbol [object Object] is; which happens to be our entry point.

[object Object] is our function that will be defined in our [object Object] file. [object Object] declares that the function is declared elsewhere.

Then, we have the [object Object] function, which calls the [object Object] function and halts the CPU using the [object Object] instruction. Interrupts can awake the CPU from an [object Object] instruction. So we disable interrupts beforehand using [object Object] instruction. [object Object] is short for clear-interrupts.

We should ideally set aside some memory for the stack and point the stack pointer ([object Object]) to it. However, it seems like GRUB does this for us and the stack pointer is already set at this point. But, just to be sure, we will allocate some space in the BSS section and point the stack pointer to the beginning of the allocated memory. We use the [object Object] instruction which reserves memory given in bytes. After it, a label is left which will point to the edge of the reserved piece of memory. Just before the [object Object] is called, the stack pointer ([object Object]) is made to point to this space using the [object Object] instruction.

**The kernel in C**

In [object Object], we made a call to the function [object Object]. So our C code will start executing at [object Object]:

*/*
* kernel.c

*/*void kmain(void){const  char  *str =  "my first kernel";char  *vidptr =  (char*)0xb8000; *//video mem begins here.*unsigned  int i =  0;unsigned  int j =  0;*/* this loops clears the screen

* there are 25 lines each of 80 columns; each element takes 2 bytes */*while(j <  80  *  25  *  2)  {*/* blank character */*vidptr[j]  =  ' ';*/* attribute-byte - light grey on black screen */*vidptr[j+1]  =  0x07; j = j +  2;}j =  0;*/* this loop writes the string to video memory */*while(str[j]  !=  '\0')  {*/* the character's ascii */*vidptr[i]  = str[j];*/* attribute-byte: give character black bg and light grey fg */*vidptr[i+1]  =  0x07;++j;i = i +  2;}return;}

All our kernel will do is clear the screen and write to it the string “my first kernel”.

First we make a pointer [object Object] that points to the address **0xb8000**. This address is the start of video memory in protected mode. The screen’s text memory is simply a chunk of memory in our address space. The memory mapped input/output for the screen starts at 0xb8000 and supports 25 lines, each line contain 80 ascii characters.

Each character element in this text memory is represented by 16 bits (2 bytes), rather than 8 bits (1 byte) which we are used to.  The first byte should have the representation of the character as in ASCII. The second byte is the [object Object]. This describes the formatting of the character including attributes such as color.

To print the character [object Object] in green color on black background, we will store the character [object Object] in the first byte of the video memory address and the value 0x02 in the second byte.

[object Object] represents black background and [object Object] represents green foreground.

Have a look at table below for different colors:

0 - Black, 1 - Blue, 2 - Green, 3 - Cyan, 4 - Red, 5 - Magenta, 6 - Brown, 7 - Light Grey, 8 - Dark Grey, 9 - Light Blue, 10/a - Light Green, 11/b - Light Cyan, 12/c - Light Red, 13/d - Light Magenta, 14/e - Light Brown, 15/f – White.

In our kernel, we will use light grey character on a black background. So our attribute-byte must have the value 0x07.

In the first while loop, the program writes the blank character with 0x07 attribute all over the 80 columns of the 25 lines. This thus clears the screen.

In the second while loop, characters of the null terminated string “my first kernel” are written to the chunk of video memory with each character holding an attribute-byte of 0x07.

This should display the string on the screen.

**The linking part**

We will assemble [object Object] with NASM to an object file; and then using GCC we will compile [object Object] to another object file. Now, our job is to get these objects linked to an executable bootable kernel.

For that, we use an explicit linker script, which can be passed as an argument to [object Object] (our linker).

*/*
* link.ld

*/*OUTPUT_FORMAT(elf32-i386)ENTRY(start)SECTIONS {  .  =  0x100000;  .text :  {  *(.text)  }  .data :  {  *(.data)  }  .bss :  {  *(.bss)  }  }

First, we set the **output format** of our output executable to be 32 bit [Executable and Linkable Format](http://elinux.org/Executable_and_Linkable_Format_(ELF)) (ELF). ELF is the standard binary file format for Unix-like systems on x86 architecture.

**ENTRY** takes one argument. It specifies the symbol name that should be the entry point of our executable.

**SECTIONS** is the most important part for us. Here, we define the layout of our executable. We could specify how the different sections are to be merged and at what location each of these is to be placed.

Within the braces that follow the SECTIONS statement, the period character (.) represents the** location counter**.

The location counter is always initialized to 0x0 at beginning of the SECTIONS block. It can be modified by assigning a new value to it.

Remember, earlier I told you that kernel’s code should start at the address 0x100000. So, we set the location counter to 0x100000.

Have look at the next line **.text : { *(.text) }**

The asterisk (*) is a wildcard character that matches any file name. The expression[object Object] thus means all [object Object] input sections from all input files.

So, the linker merges all text sections of the object files to the executable’s text section, at the address stored in the location counter. Thus, the code section of our executable begins at 0x100000.

After the linker places the text output section, the value of the location counter will become

0x1000000 + the size of the text output section.

Similarly, the data and bss sections are merged and placed at the then values of location-counter.

**Grub and Multiboot**

Now, we have all our files ready to build the kernel. But, since we like to boot our kernel with the [GRUB bootloader](http://www.gnu.org/software/grub/), there is one step left.

There is a standard for loading various x86 kernels using a boot loader; called as **Multiboot specification**.

GRUB will only load our kernel if it complies with the [Multiboot spec](http://www.gnu.org/software/grub/manual/multiboot/multiboot.html).

According to the spec, the kernel must contain a header (known as Multiboot header) within its first 8 KiloBytes.

Further, This Multiboot header must contain 3 fields that are 4 byte aligned namely:

    - a **magic** field: containing the magic number **0x1BADB002**, to identify the header.
    - a **flags** field: We will not care about this field. We will simply set it to zero.
    - a **checksum** field: the checksum field when added to the fields ‘magic’ and ‘flags’ must give zero.

So our [object Object] will become:
;;kernel.asm;nasm directive -  32 bit
bits 32section .text ;multiboot spec
align 4 dd 0x1BADB002  ;magic
dd 0x00  ;flags

dd -  (0x1BADB002  +  0x00)  ;checksum. m+f+c should be zeroglobal startextern kmain ;kmain is  defined  in the c file

start: cli;block interrupts
mov esp, stack_space;set stack pointer
call kmain
hlt;halt the CPU
section .bss
resb 8192;8KB  for stack
stack_space:
The **dd** defines a double word of size 4 bytes.

**Building the kernel**

We will now create object files from [object Object] and [object Object] and then link it using our linker script.

nasm -f elf32 kernel.asm -o kasm.o
will run the assembler to create the object file kasm.o in ELF-32 bit format.
gcc -m32 -c kernel.c -o kc.o

The ’-c ’ option makes sure that after compiling, linking doesn’t implicitly happen.

ld -m elf_i386 -T link.ld -o kernel kasm.o kc.o

will run the linker with our linker script and generate the executable named **kernel**.

**Configure your grub and run your kernel**

GRUB requires your kernel to be of the name pattern [object Object]. So, rename the kernel. I renamed my kernel executable to kernel-701.

Now place it in the **/boot** directory. You will require superuser privileges to do so.

In your GRUB configuration file [object Object] you should add an entry, something like:

title myKernel
root (hd0,0)
kernel /boot/kernel-701 ro

Don’t forget to remove the directive [object Object] if it exists.

Reboot your computer, and you’ll get a list selection with the name of your kernel listed.

Select it and you should see:
![image](../_resources/44b089c89264683c7dd5f813da925dad.png)

That’s your kernel!!

**PS:
**

* It’s always advisable to get yourself a virtual machine for all kinds of kernel hacking. * To run this on **grub2 **which is the default bootloader for newer distros, your config should look like this:

menuentry 'kernel 7001'  {set root='hd0,msdos1'multiboot /boot/kernel-7001 ro}

* Also, if you want to run the kernel on the [object Object] emulator instead of booting with GRUB, you can do so by:

qemu-system-i386 -kernel kernel
Also, see the next article in the Kernel series:

[Kernel 201 - Let’s write a Kernel with keyboard and screen support](http://arjunsreedharan.org/post/99370248137/kernel-201-lets-write-a-kernel-with-keyboard-and)

**References and Thanks**
    1. 1. [wiki.osdev.org](http://wiki.osdev.org/)
    2. 2. [osdever.net](http://www.osdever.net/)

    3. 3. [Multiboot spec](http://www.gnu.org/software/grub/manual/multiboot/multiboot.html)

    4. 4. Thanks to [Rubén Laguna](http://rubenlaguna.com/) from comments for grub2 config