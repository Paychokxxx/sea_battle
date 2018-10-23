class Battlefield():
    def __init__(self, horizontal_length, vertical_length):
        self.horizontal_length = horizontal_length
        self.vertical_length = vertical_length
        #print("Parent Constructor called")
    
    def create_field(self):
        field = []

        # create " ".1.2.3.4.5.6.7.8.9.10 vertical coordinates
        for i in range(self.vertical_length+1):
            if i == 0: 
                field.append(['  '])
            elif i >= 10:
                field.append([str(i)])
            else:
                field.append([' '+ str(i)])

        # [' ABCDEFGHIJ'] created first element of list, top coordinates
        before_first_letter_number = 65
        for i in range(self.horizontal_length):
            if i == 0:
                field[0].append(chr(before_first_letter_number))
            else:
                field[0].append(chr(before_first_letter_number+i))

        # adding empty "0" fields to map         
        while len(field[1]) < self.vertical_length+1:

            for y in range(self.vertical_length):
                field[y+1] += ' '

        return field