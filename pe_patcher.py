import pefile

SUCCESS_MESSAGE = "Patched successfully!"

def enable_4GB(file_path: str) -> str:
    try:
        pe = pefile.PE(file_path, fast_load=True)
        # Making a backup
        pe.write(filename=(file_path + ".Backup"))

        # Changing the IMAGE_FILE_LARGE_ADDRESS_AWARE flag
        pe.FILE_HEADER.Characteristics = pe.FILE_HEADER.Characteristics | 0x20

        # Regenerating checksum
        pe.OPTIONAL_HEADER.CheckSum = pe.generate_checksum()

        # Saving the file
        pe.write(filename=file_path)

        return SUCCESS_MESSAGE
    except OSError as e:
        return e
    except pefile.PEFormatError as e:
        return "[-] PEFormatError: %s" % e.value
