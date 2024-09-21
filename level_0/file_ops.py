from typing import TextIO


class file_ops:
    def __init__(self, level: int, file_number: int,
                 parse_example: bool = True, parse_level: bool = True,
                 delimiter: str = ' ',
                 input_file_schema: str = "level{level}_{number}.in",
                 output_file_schema: str = "level{level}_{number}.out"):
        # info
        self._level: int = level
        self._file_number: int = file_number
        self._parse_example: bool = parse_example
        self._parse_level: bool = parse_level
        self._delimiter: str = delimiter

        # file schemas
        self._input_file_schema: str = input_file_schema
        self._output_file_schema: str = output_file_schema

        # file operation members
        self._fd: TextIO = TextIO()
        self._rows: int = 0
        self._cols: int = 0
        self._output_ios: list[TextIO] = []

    def readFiles(self) -> list:
        data = []

        if self._parse_example:
            filetoread = self._input_file_schema.format(level=self._level, number="example")
            data.append(self.readFile(filetoread))
        if self._parse_level:
            for i in range(1, self._file_number + 1):
                filetoread = self._input_file_schema.format(level=self._level, number=str(i))
                data.append(self.readFile(filetoread))

        return data

    def readFile(self, infile: str):
        self._fd = open(infile, 'r')
        self.readHeader()
        parsed = self.parseBody()
        self._fd.close()
        return parsed

    def readHeader(self) -> None:
        header = self._fd.readline()
        options = header.split(self._delimiter)
        self._rows = int(options[0])
        self._cols = int(options[1])

    def parseBody(self):
        data = []
        for i in range(self._rows):
            line = self._fd.readline()
            data.append(line.split(self._delimiter))
        return data

    def getOutputIO(self) -> list[TextIO]:
        if len(self._output_ios) is not 0:
            print("Output IOs already open")
            return self._output_ios

        if self._parse_example:
            filetoread = self._output_file_schema.format(level=self._level, number="example")
            self._output_ios.append(open(filetoread, 'w'))
        if self._parse_level:
            for i in range(1, self._file_number + 1):
                filetoread = self._output_file_schema.format(level=self._level, number=str(i))
                self._output_ios.append(open(filetoread, 'w'))

        return self._output_ios

    def closeOutputIO(self) -> None:
        for io in self._output_ios:
            io.close()

        self._output_ios.clear()
        return
