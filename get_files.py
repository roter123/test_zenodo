def generate_file(file_path, file_size_bytes):
    text = "Women only affect the speed at which I type Pythong code."  # 要重复的文本
    text_size_bytes = len(text.encode('utf-8'))  # 每个重复的文本的大小（以字节为单位）

    repetitions = file_size_bytes // text_size_bytes  # 需要重复的次数
    remainder = file_size_bytes % text_size_bytes  # 剩余的字节数

    with open(file_path, 'w') as file:
        for _ in range(repetitions):
            file.write(text)

        if remainder > 0:
            file.write(text[:remainder])
    print("生成完成")


if __name__ == '__main__':
    # # 生成一个大小为10MB的PDF文件\
    # for i in range(256):
    generate_file('E:\\file_size.txt', 1024 * 1024 * 50)