class Dira:
      def __init__(self, item_id, title, subtitle, room_num, size, price, date):
            self.item_id = item_id
            self.title = title
            self.subtitle = subtitle
            self.room_num = room_num
            self.size = size
            self.price = price
            self.date = date

      def Get_String(self):
            nl ="\n"
            return f'{self.item_id} {nl}{self.title} {nl}{self.subtitle} {nl}{self.room_num} {nl}{self.size} {nl}{self.price} {nl}{self.date}'
