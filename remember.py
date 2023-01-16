from speak import speak
def rememberfunciton():
    with open('data.txt') as f:
                lines = f.read()
                speak('As I recall you told me that ,'+ lines)
                