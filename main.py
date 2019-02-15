


class main:
    def Size():
        global Tile_Size
        Tile_Size = 0
        while not(Tile_Size) in (range(7, 11)):
            Tile_Size = int(input("wählen sie eine Spielfeld Größe von 7-10:"))
        return Tile_Size

    def Mode():
        global Game_Mode
        Game_Mode = ""
        while Game_Mode.lower() != "singelplayer" and Game_Mode.lower() != "multiplayer":
            Game_Mode = input("Spielmodus:")
        return Game_Mode
    Tile_Size = Size()
    Game_Mode = Mode()

class Options:


class Ships:
    def Ship_ammount():
        if Tile_Size == 7:
            q, w, e, r = 0,1,2,1         #q is for 5er; w is for 4er;e is for 3er;r is dor 2er
            return q, w, e, r
        elif Tile_Size == 8:
            q, w, e, r = 1,1,1,1
            return q, w, e, r
        elif Tile_Size == 9:
            q, w, e, r = 1,1,2,1
            return q, w, e, r
        elif Tile_Size == 10:
            q, w, e, r =1,2,2,1
            return q, w, e, r

    Ship_ammount()

main_main = main()
main_Ships = Ships()

print("Ende")