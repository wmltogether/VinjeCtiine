# -*- coding: utf-8 -*-
# It's an IronPython script
import os,codecs,struct
import zlib
import math
from cStringIO import StringIO

class util:
    def __init__(self):
        pass


class ProgramHeader:
    def __init__(self):
        self.p_type = None      # 00h Elf32_Word    , segment type
        self.p_offset = None    # 04h Elf32_Off     , segment offset
        self.p_vaddr = None     # 08h Elf32_Addr    , virtual address
        self.p_paddr = None     # 0ch Elf32_Addr    , physical address
        self.p_filesz = None    # 10h Elf32_Word    , number of bytes in file
        self.p_memsz = None     # 14h Elf32_Word    , number of bytes in mem
        self.p_flags = None     # 18h Elf32_Word    , flags
        self.p_align = None     # 1ch Elf32_Word    , memory alignment

class SectionHeader:
    def __init__(self):
        self.sh_name = None     # 00h Elf32_Word    , name
        self.sh_type = None     # 04h Elf32_Word    , type
        self.sh_flags = None
        self.sh_addr = None     # 10h Elf32_Word    , address
        self.sh_offset = None   # 14h Elf32_Word    , file offset
        self.sh_size = None     # 18h Elf32_Word    , section size
        self.sh_link = None
        self.sh_info = None
        self.sh_addralign = None
        self.sh_entsize = None  # 24h Elf32_Word    , section entry size

class Rpx:
    def __init__(self):
        # RPX is a compressed ELF.All sections are compressed by zlib.
        self.e_endian = ">" #always big
        self.e_ident = None     # 00h unsigned char , ELF Identification
        self.e_type = None      # 10h Elf32_Half    , object file type
        self.e_machine = None   # 12h Elf32_Half    , machine
        self.e_version = None   # 14h Elf32_Word    , object file version
        self.e_entry = None     # 18h Elf32_Addr    , virtual entry point
        self.e_phoff = None     # 1ch Elf32_Off     , program header table offset
        self.e_shoff = None     # 20h Elf32_Off     , section header table offset
        self.e_flag = None      # 24h Elf32_Word    , processor-specific flags
        self.e_ensize = None    # 28h Elf32_Half    , ELF Header size
        self.e_phentsize = None # 2ah Elf32_Half    , program header entry size
        self.e_phnum = None     # 2ch Elf32_Half    , number of program header entries
        self.e_shentsize = None # 2eh Elf32_Half    , section header entry size
        self.e_shnum = None     # 30h Elf32_Half    , number of section header entries
        self.e_shstrndx = None  # 32h Elf32_Half    , section header table's "section header string table" entry offset
        self.e_fullMemorySize = None
        self.e_SectionStringTableOffset = None
        self.e_shstrIndexOffset = None # Point to shstr Index Address
        self.e_firstPT_LOAD_OFFSET = None
        self.elf_section_list = []

        
    def _ReadRPXSectionInfo(self, rpx_name):
        print("*Loading  TABLE")
        fp = open(rpx_name , 'rb')
        fp.seek(0x10)
        (self.e_type , self.e_machine , \
            self.e_version , self.e_entry , self.e_phoff , \
            self.e_shoff , self.e_flag , self.e_ensize ,\
            self.e_phentsize , self.e_phnum , self.e_shentsize ,\
            self.e_shnum , self.e_shstrndx )= struct.unpack("%sHHIIIIIHHHHHH"%self.e_endian ,fp.read(0x24))
        if self.e_phoff != 0:
            fp.seek(self.e_phoff)
            for i in xrange(self.e_phnum):
                pHeader = ProgramHeader()
                (pHeader.p_type , pHeader.p_offset , pHeader.p_vaddr , pHeader.p_paddr , \
                    pHeader.p_filesz , pHeader.p_memsz ,pHeader.p_flags, pHeader.p_align) = struct.unpack("%s8I"%self.e_endian ,fp.read(0x20))
                if pHeader.p_type == 1 and pHeader.p_flags == 5:
                    # get PT_LOAD
                    self.e_firstPT_LOAD_OFFSET = fp.tell() - 0x20
                if pHeader.p_type == 1 and pHeader.p_flags == 6:
                    # get full memory length of ELF
                    self.e_fullMemorySize = (((pHeader.p_vaddr + pHeader.p_memsz)/pHeader.p_align) | 1) * pHeader.p_align
        fp.seek(self.e_shoff + self.e_shstrndx * self.e_shentsize)
        self.e_shstrIndexOffset = self.e_shoff
        shHeader = SectionHeader()
        (shHeader.sh_name ,
             shHeader.sh_type ,
             shHeader.sh_flags ,
             shHeader.sh_addr ,
             shHeader.sh_offset ,
             shHeader.sh_size,
             shHeader.sh_link,
             shHeader.sh_info ,
             shHeader.sh_addralign,
             shHeader.sh_entsize) = struct.unpack("%s10I"%self.e_endian ,fp.read(0x28))
        fp.seek(self.e_shoff)
        for i in xrange(self.e_shnum):
            shHeader = SectionHeader()
            (shHeader.sh_name ,
             shHeader.sh_type ,
             shHeader.sh_flags ,
             shHeader.sh_addr ,
             shHeader.sh_offset ,
             shHeader.sh_size,
             shHeader.sh_link,
             shHeader.sh_info ,
             shHeader.sh_addralign,
             shHeader.sh_entsize) = struct.unpack("%s10I"%self.e_endian ,fp.read(0x28))

            print("%08x\t%08x\t%08x\t%08x\t%08x\t%08x\t%08x\t%08x\t%08x"%(
                                                                    shHeader.sh_type ,
                                                                    shHeader.sh_flags ,
                                                                    shHeader.sh_addr ,
                                                                    shHeader.sh_offset ,
                                                                    shHeader.sh_size,
                                                                    shHeader.sh_link,
                                                                    shHeader.sh_info ,
                                                                    shHeader.sh_addralign,
                                                                    shHeader.sh_entsize))
                                                                    
            self.elf_section_list.append(shHeader)
                                                                    
        fp.close()
        pass

class Elf:
    def __init__(self):
        # VC ROM always in .rodata section
        self.e_endian = ">" #always big
        self.e_ident = None     # 00h unsigned char , ELF Identification
        self.e_type = None      # 10h Elf32_Half    , object file type
        self.e_machine = None   # 12h Elf32_Half    , machine
        self.e_version = None   # 14h Elf32_Word    , object file version
        self.e_entry = None     # 18h Elf32_Addr    , virtual entry point
        self.e_phoff = None     # 1ch Elf32_Off     , program header table offset
        self.e_shoff = None     # 20h Elf32_Off     , section header table offset
        self.e_flag = None      # 24h Elf32_Word    , processor-specific flags
        self.e_ensize = None    # 28h Elf32_Half    , ELF Header size
        self.e_phentsize = None # 2ah Elf32_Half    , program header entry size
        self.e_phnum = None     # 2ch Elf32_Half    , number of program header entries
        self.e_shentsize = None # 2eh Elf32_Half    , section header entry size
        self.e_shnum = None     # 30h Elf32_Half    , number of section header entries
        self.e_shstrndx = None  # 32h Elf32_Half    , section header table's "section header string table" entry offset
        self.e_fullMemorySize = None
        self.e_SectionStringTableOffset = None
        self.e_shstrIndexOffset = None # Point to shstr Index Address
        self.e_firstPT_LOAD_OFFSET = None
        self.elf_section_list = []
        pass
    
    def _ReadElf(self ,elf_name):
        print("*Loading ELF TABLE")
        fp = open(elf_name , 'rb')
        fp.seek(0x10)
        (self.e_type , self.e_machine , \
            self.e_version , self.e_entry , self.e_phoff , \
            self.e_shoff , self.e_flag , self.e_ensize ,\
            self.e_phentsize , self.e_phnum , self.e_shentsize ,\
            self.e_shnum , self.e_shstrndx )= struct.unpack("%sHHIIIIIHHHHHH"%self.e_endian ,fp.read(0x24))
        if self.e_phoff != 0:
            fp.seek(self.e_phoff)
            for i in xrange(self.e_phnum):
                pHeader = ProgramHeader()
                (pHeader.p_type , pHeader.p_offset , pHeader.p_vaddr , pHeader.p_paddr , \
                    pHeader.p_filesz , pHeader.p_memsz ,pHeader.p_flags, pHeader.p_align) = struct.unpack("%s8I"%self.e_endian ,fp.read(0x20))
                if pHeader.p_type == 1 and pHeader.p_flags == 5:
                    # get PT_LOAD
                    self.e_firstPT_LOAD_OFFSET = fp.tell() - 0x20
                if pHeader.p_type == 1 and pHeader.p_flags == 6:
                    # get full memory length of ELF
                    self.e_fullMemorySize = (((pHeader.p_vaddr + pHeader.p_memsz)/pHeader.p_align) | 1) * pHeader.p_align
        fp.seek(self.e_shoff + self.e_shstrndx * self.e_shentsize)
        self.e_shstrIndexOffset = self.e_shoff 
        shHeader = SectionHeader()
        (shHeader.sh_name ,
             shHeader.sh_type ,
             shHeader.sh_flags ,
             shHeader.sh_addr ,
             shHeader.sh_offset ,
             shHeader.sh_size,
             shHeader.sh_link,
             shHeader.sh_info ,
             shHeader.sh_addralign,
             shHeader.sh_entsize) = struct.unpack("%s10I"%self.e_endian ,fp.read(0x28))
        fp.seek(shHeader.sh_offset)
        self.e_SectionStringTableOffset = shHeader.sh_offset
        SectionStringTable = fp.read(shHeader.sh_size)
        fp.seek(self.e_shoff)
        for i in xrange(self.e_shnum):
            shHeader = SectionHeader()
            (shHeader.sh_name ,
             shHeader.sh_type ,
             shHeader.sh_flags ,
             shHeader.sh_addr ,
             shHeader.sh_offset ,
             shHeader.sh_size,
             shHeader.sh_link,
             shHeader.sh_info ,
             shHeader.sh_addralign,
             shHeader.sh_entsize) = struct.unpack("%s10I"%self.e_endian ,fp.read(0x28))
            shHeader.sh_name = SectionStringTable[shHeader.sh_name:].split("\x00")[0]
            print("%s\n%08x\t%08x\t%08x\t%08x\t%08x\t%08x\t%08x\t%08x\t%08x"%(shHeader.sh_name,
                                                                    shHeader.sh_type ,
                                                                    shHeader.sh_flags ,
                                                                    shHeader.sh_addr ,
                                                                    shHeader.sh_offset ,
                                                                    shHeader.sh_size,
                                                                    shHeader.sh_link,
                                                                    shHeader.sh_info ,
                                                                    shHeader.sh_addralign,
                                                                    shHeader.sh_entsize))
                                                                    
            self.elf_section_list.append(shHeader)
                                                                    
        fp.close()
        pass
    
    def _FindROData(self):
        tag = ".rodata"
        for i in xrange(len(self.elf_section_list)):
            item = self.elf_section_list[i]
            if item.sh_name == tag:
                return (i,item.sh_offset,item.sh_size)
        return (0,0,0)
        
    
class VC:
    def __init__(self):
        self.WUP_TITLE_TAG = "WUP-"
        self.NES_ROM_TAG = "\x4E\x45\x53\x1A"
        self.NES_ROM_TAG2 = "\x4E\x45\x53\x00"
        self.title_postion = -1
        self.rom_position = -1
        self.container_size = 0
        self.hasNES_ROM = False
        self.hasSNES_ROM = False
        pass
    
    def _CompressSection(self, section):
        zsection = (struct.pack(">I" , len(section)) + zlib.compress(section))
        print(type(zsection))
        return zsection
        
    
    def _get_vc_container_size(self , buffer):
        if self.hasNES_ROM == True:
            buffer.seek(self.title_position - 0xe)
        elif self.hasSNES_ROM == True:
            buffer.seek(self.title_position - 0x16)
        else:
            self.container_size = 0
            return None
        chunk_size = 64
        chunk_nums = struct.unpack("H" , buffer.read(2))[0]
        self.container_size = chunk_size * chunk_nums * 1024
        

    def _findTAG_position(self , data , tag):
        pos = 0
        index = data.find(tag,pos)
        if index == -1:
            return -1
        return index

    def _checkCurrnetVC(self, ELF_NAME):
        ro_offset = 0
        container_type = ""
        rom_position = 0
        container_size = 0
        valid_container = False
        WUP_Title = ""
        
        elfTool = Elf()
        elfTool._ReadElf(ELF_NAME)
        (section_id,ro_offset,ro_size) = elfTool._FindROData()
        if not ro_offset == 0:
            fp = open(ELF_NAME , "rb")
            fp.seek(ro_offset)
            rodata_section = fp.read(ro_size)
            ro_buffer = StringIO()
            ro_buffer.write(rodata_section)
            ro_buffer.seek(0)
            self.title_position = self._findTAG_position(rodata_section , self.WUP_TITLE_TAG)
            self.rom_position = self._findTAG_position(rodata_section , self.NES_ROM_TAG)
            if self.title_position <= 0:
                return (WUP_Title,self.hasNES_ROM ,self.hasSNES_ROM ,container_size)
            if self.rom_position > 0 :
                print("Found NES ROM")
                self.hasNES_ROM = True
            else:
                print("NES ROM NOT Found.Maybe it's a SNES ROM")
                self.hasSNES_ROM = True
            title_position = self.title_position
            ro_buffer.seek(title_position)
            WUP_Title = ro_buffer.read(0x10).split("\x00")[0]
            self._get_vc_container_size(ro_buffer)
            container_size = self.container_size
            if self.container_size > 8 * 1024 * 1024 :
                print("VC SIZE error.Not a valid VC container")
                self.hasSNES_ROM = False
                self.hasNES_ROM = False
                container_size = 0
                self.container_size = 0
            return (WUP_Title,self.hasNES_ROM ,self.hasSNES_ROM ,container_size)
        return (WUP_Title,self.hasNES_ROM ,self.hasSNES_ROM ,container_size)
            
        
    def _NES_Inject(self, ROM_NAME , RPX_NAME , ELF_NAME , DEST_RPX_NAME):
        elfTool = Elf()
        rpxTool = Rpx()
        elfTool._ReadElf(ELF_NAME)
        rpxTool._ReadRPXSectionInfo(RPX_NAME)
        (section_id,ro_offset,ro_size) = elfTool._FindROData()
        if not ro_offset == 0:
            fp = open(ELF_NAME , "rb")
            fp.seek(ro_offset)
            rodata_section = fp.read(ro_size)
            ro_buffer = StringIO()
            ro_buffer.write(rodata_section)
            ro_buffer.seek(0)
            self.title_position = self._findTAG_position(rodata_section , self.WUP_TITLE_TAG)
            self.rom_position = self._findTAG_position(rodata_section , self.NES_ROM_TAG)
            if self.rom_position > 0 :
                self.hasNES_ROM = True
            else:
                self.rom_position = self.title_position + 0xc
                self.hasSNES_ROM = True
            self._get_vc_container_size(ro_buffer)
            rom_file = open(ROM_NAME , 'rb')
            data = rom_file.read()
            if ROM_NAME[-4:].lower() == ".smc" and os.path.getsize(ROM_NAME)%0x1000 != 0:
                data = data[0x200:]
            rom_file.close()
            currentRomSize = len(data)
            if self.container_size > 0 and currentRomSize <= self.container_size:
                # do inject
                print("injecting")
                ro_buffer.seek(self.rom_position)
                ro_buffer.write(data)
                ro_buffer.write("\x00" * (self.container_size - currentRomSize))
                rodata_section = ro_buffer.getvalue()
                zlib_section = self._CompressSection(rodata_section)
                current_header = rpxTool.elf_section_list[section_id]
                current_zoffset = current_header.sh_offset
                current_zsize = current_header.sh_size
                print("current zsize : %08x;\noriginal zsize : %08x"%(len(zlib_section),current_zsize))
                if len(zlib_section) <= current_zsize:
                    print("compressing")
                    rpx_file = open(RPX_NAME , "rb")
                    rpx_buffer = StringIO()
                    rpx_buffer.write(rpx_file.read())
                    rpx_file.close()
                    rpx_buffer.seek(0)
                    rpx_buffer.seek(current_zoffset)
                    rpx_buffer.write(zlib_section)
                    rpx_buffer.write("\x00" * (current_zsize - len(zlib_section)))
                    print("e_shstrIndexOffset:%08x"%rpxTool.e_shstrIndexOffset)
                    index = rpxTool.e_shstrIndexOffset + 0x28 * section_id + 0x4 * 5
                    print("fixing at:%08x >> write chunk size %08x"%(index,len(zlib_section)))
                    rpx_buffer.seek(index)
                    rpx_buffer.write(struct.pack(">I" , len(zlib_section)))
                    dest_rpx_file = open( DEST_RPX_NAME , "wb")
                    dest_rpx_file.write(rpx_buffer.getvalue())
                    dest_rpx_file.close()
                    return 0
                else:
                    print("error:zlib chunk size is too small")
                    
                    return 1
            else:
                print("error:container_size is too small")
                return 2
        return 3

