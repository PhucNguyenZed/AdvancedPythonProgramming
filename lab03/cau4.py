def process_file(reader):
    def skip_header(reader):
        reader=(open,'r')
        reader.close
        return reader
    line = skip_header(reader).strip()
    print(line)  
    print(reader.read('alkaline_metals.txt'))
