#Names:Ivan and Nora
#Date:7/15
#Pokemon Simulator

#Initialize

#Global variables
pokemon_level=0
pokemon_name=""
#Functions
#Main
print("Welcome to the Pokemon Evolution Simulator.\nChoose one to be your starter Pokemon\n1. Bulbasur\n2. Charmander\n3. Squirtle\n")
option=input("Option: ")
if option=="1":
    print("You chose Bulbasaur!\n")
    pokemon_name="Bulbasaur"
elif option=="2":
    print("You chose Charmander!\n")
    pokemon_name="Charmander"
elif option=="3":
    print("You chose Squirtle!\n")
    pokemon_name="Squirtle"
else:
    print("error\n")
while True:
    print("What would you like to do next?\n1. Train\n2. Gym Battle\n3. Display Pokemon info\n4. Quit\n")
    choice=input("Option: ")
    if choice=="1":
        pokemon_level=pokemon_level+1
        print("You trained "+pokemon_name+"!\n")
    elif choice=="2":
        pokemon_level=pokemon_level+2
        print(pokemon_name+" fought at the gym!\n")
    elif choice=="3":
        print(pokemon_name)
        print("Level "+ str(pokemon_level) + "\n")
        if pokemon_name == "Bulbasaur":
            print("                                           /\\n");
            print("                        _,.------....___,.' ',.-.\n");
            print("                     ,-'          _,.--\"        |\n");
            print("                   ,'         _.-'              .\n");
            print("                  /   ,     ,'                   `\n");
            print("                 .   /     /                     ``.\n");
            print("                 |  |     .                       \\.\\\n");
            print("       ____      |___._.  |       __               \\ `.\n");
            print("     .'    `---\"\"       ``\"-.--\"'`  \\               .  \\\n");
            print("    .  ,            __               `              |   .\n");
            print("    `,'         ,-\"'  .               \\             |    L\n");
            print("   ,'          '    _.'                -._          /    |\n");
            print("  ,`-.    ,\".   `--'                      >.      ,'     |\n");
            print(" . .'\\'   `-'       __    ,  ,-.         /  `.__.-      ,'\n");
            print(" ||:, .           ,'  ;  /  / \\ `        `.    .      .'/\n");
            print(" j|:D  \\          `--'  ' ,'_  . .         `.__, \\   , /\n");
            print("/ L:_  |                 .  \"' :_;                `.'.'\n");
            print(".    \"\"'                  \"\"\"\"\"'                    V\n");
            print(" `.                                 .    `.   _,..  `\n");
            print("   `,_   .    .                _,-'/    .. `,'   __  `\n");
            print("    ) \\`._        ___....----\"'  ,'   .'  \\ |   '  \\  .\n");
            print("   /   `. \"`-.--\"'         _,' ,'     `---' |    `./  |\n");
            print("  .   _  `\"\"'--.._____..--\"   ,             '         |\n");
            print("  | .\" `. `-.                /-.           /          ,\n");
            print("  | `._.'    `,_            ;  /         ,'          .\n");
            print(" .'          /| `-.        . ,'         ,           ,\n");
            print(" '-.__ __ _,','    '`-..___;-...__   ,.'\\ ____.___.'\n");
            print(" `\"^--'..'   '-`-^-'\"--    `-^-'`.''\"\"\"\"\"`.,^.`.--' mh\n");
            print("\n");
            print("\n");
        elif pokemon_name == "Ivysaur":
            print("                               ,'\"`.,./.\n");
            print("                             ,'        Y',\"..\n");
            print("                           ,'           \\  | \\\n");
            print("                          /              . |  `\n");
            print("                         /               | |   \\\n");
            print("            __          .                | |    .\n");
            print("       _   \\  `. ---.   |                | j    |\n");
            print("      / `-._\\   `Y   \\  |                |.     |\n");
            print("     _`.    ``    \\   \\ |..              '      |,-'\"\"7,....\n");
            print("     l     '-.     . , `|  | , |`. , ,  /,     ,'    '/   ,'_,.-.\n");
            print("     `-..     `-.  : :     |/ `   ' \"\\,' | _  /          '-'    /___\n");
            print("      \\\"\"' __.,.-`.: :        /   /._    l'.,'\n");
            print("       `--,   _.-' `\".           /__ `'-.' '         .\n");
            print("       ,---..._,.--\"\"\"\"\"\"\"--.__..----,-.'   .  /    .'   ,.--\n");
            print("       |                          ,':| /    | /     ;.,-'--      ,.-\n");
            print("       |     .---.              .'  :|'     |/ ,.-='\"-.`\"`' _   -.'\n");
            print("       /    \\    /               `. :|--.  _L,\"---.._        \"----'\n");
            print("     ,' `.   \\ ,'           _,     `''   ``.-'       `-  -..___,'\n");
            print("    . ,.  .   `   __     .-'  _.-           `.     .__    \\\n");
            print("    |. |`        \"  ;   !   ,.  |             `.    `.`'---'\n");
            print("    ,| |C\\       ` /    | ,' |(]|            -. |-..--`\n");
            print("   /  \"'--'       '      /___|__]        `.  `- |`.\n");
            print("  .       ,'                   ,   /       .    `. \\\n");
            print("    \\                      .,-'  ,'         .     `-.\n");
            print("     x---..`.  -'  __..--'\"/\"\"\"\"\"  ,-.      |   |   |\n");
            print("    / \\--._'-.,.--'     _`-    _. ' /       |     -.|\n");
            print("   ,   .   `-..__ ...--'  _,.-' | `   ,.-.  ;   /  '|\n");
            print("  .  _,'         '\"-----\"\"      |    `   | /  ,'    ;\n");
            print("  |-'  .-.    `._               |     `._// ,'     /\n");
            print(" _|    `-'   _,' \"`--.._________|        `,'    _ /.\n");
            print("//\\   ,-._.'\"/\\__,.   _,\"     /_\\__/`. /'.-.'.-/_,`-' mh\n");
            print("`-\"`\"' v'    `\"  `-`-\"              `-'`-`  `'\n");
        elif pokemon_name == "Venusaur":
            print("                           _._       _,._\n");
            print("                        _.'   `. ' .'   _`.\n");
            print("                ,\"\"\"/`\"\"-.-.,/. ` V'\\-,`.,--/\"\"\".\"-..\n");
            print("              ,'    `...,' . ,\\-----._|     `.   /   \\\n");
            print("             `.            .`  -'`\"\" .._   :> `-'   `.\n");
            print("            ,'  ,-.  _,.-'| `..___ ,'   |'-..__   .._ L\n");
            print("           .    \\_ -'   `-'     ..      `.-' `.`-.'_ .|\n");
            print("           |   ,',-,--..  ,--../  `.  .-.    , `-.  ``.\n");
            print("           `.,' ,  |   |  `.  /'/,,.\\/  |    \\|   |\n");
            print("                `  `---'    `j   .   \\  .     '   j\n");
            print("              ,__`\"        ,'|`'\\_/`.'\\'        |\\-'-, _,.\n");
            print("       .--...`-. `-`. /    '- ..      _,    /\\ ,' .--\"'  ,'\".\n");
            print("     _'-\"\"-    --  _`'-.../ __ '.'`-^,_`-\"\"\"\"---....__  ' _,-`\n");
            print("   _.----`  _..--.'        |  \"`-..-\" __|'\"'         .\"\"-. \"\"'--.._\n");
            print("  /        '    /     ,  _.+-.'  ||._'   \"\"\"\". .          `     .__\\\n");
            print(" `---    /        /  / j'       _/|..`  -. `-`\\ \\   \\  \\   `.  \\ `-..\n");
            print(",\" _.-' /    /` ./  /`_|_,-\"   ','|       `. | -'`._,   L  \\ .  `.   |\n");
            print("`\"' /  /  / ,__...-----| _.,  ,'            `|----.._`-.|' |. .` ..  .\n");
            print("   /  '| /.,/   \\--.._ `-,' ,          .  '`.'  __,., '  ''``._ \\ \\`,'\n");
            print("  /_,'---  ,     \\`._,-` \\ //  / . \\    `._,  -`,  / / _   |   `-L -\n");
            print("   /       `.     ,  ..._ ' `_/ '| |\\ `._'       '-.'   `.,'     |\n");
            print("  '         /    /  ..   `.  `./ | ; `.'    ,\"\" ,.  `.    \\      |\n");
            print("   `.     ,'   ,'   | |\\  |       \"        |  ,'\\ |   \\    `    ,L\n");
            print("   /|`.  /    '     | `-| '                  /`-' |    L    `._/  \\\n");
            print("  / | .`|    |  .   `._.'                   `.__,'   .  |     |  (`\n");
            print(" '-\"\"-'_|    `. `.__,._____     .    _,        ____ ,-  j     \".-'\"'\n");
            print("        \\      `-.  \\/.    `\"--.._    _,.---'\"\"\\/  \"_,.'     /-'\n");
            print("         )        `-._ '-.        `--\"      _.-'.-\"\"        `.\n");
            print("        ./            `,. `\".._________...\"\"_.-\"`.          _j\n");
            print("       /_\\.__,\"\".   ,.'  \"`-...________.---\"     .\".   ,.  / \\\n");
            print("              \\_/\"\"\"-'                           `-'--(_,`\"`-` mh\n");
        elif pokemon_name == "Charmander":
            print("              _.--\"\"`-..\n");
            print("            ,'          `.\n");
            print("          ,'          __  `.\n");
            print("         /|          \" __   \\\n");
            print("        , |           / |.   .\n");
            print("        |,'          !_.'|   |\n");
            print("      ,'             '   |   |\n");
            print("     /              |`--'|   |\n");
            print("    |                `---'   |\n");
            print("     .   ,                   |                       ,\".\n");
            print("      ._     '           _'  |                    , ' \\ `\n");
            print("  `.. `.`-...___,...---\"\"    |       __,.        ,`\"   L,|\n");
            print("  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \\\n");
            print("-:..     `. `-..--_.,.<       `\"      / `.        `-/ |   .\n");
            print("  `,         \"\"\"\"'     `.              ,'         |   |  ',,\n");
            print("    `.      '            '            /          '    |'. |/\n");
            print("      `.   |              \\       _,-'           |       ''\n");
            print("        `._'               \\   '\"\\                .      |\n");
            print("           |                '     \\                `._  ,'\n");
            print("           |                 '     \\                 .'|\n");
            print("           |                 .      \\                | |\n");
            print("           |                 |       L              ,' |\n");
            print("           `                 |       |             /   '\n");
            print("            \\                |       |           ,'   /\n");
            print("          ,' \\               |  _.._ ,-..___,..-'    ,'\n");
            print("         /     .             .      `!             ,j'\n");
            print("        /       `.          /        .           .'/\n");
            print("       .          `.       /         |        _.'.'\n");
            print("        `.          7`'---'          |------\"'_.'\n");
            print("       _,.`,_     _'                ,''-----\"'\n");
            print("   _,-_    '       `.     .'      ,\\\n");
            print("   -\" /`.         _,'     | _  _  _.|\n");
            print("    \"\"--'---\"\"\"\"\"'        `' '! |! /\n");
            print("                            `\" \" -' mh\n");
            print("\n");
            print("\n");
        elif pokemon_name == "Charmeleon":
            print("                      ,-'`\\\n");
            print("                  _,\"'    j\n");
            print("           __....+       /               .\n");
            print("       ,-'\"             /               ; `-._.'.\n");
            print("      /                (              ,'       .'\n");
            print("     |            _.    \\             \\   ---._ `-.\n");
            print("     ,|    ,   _.'  Y    \\             `- ,'   \\   `.`.\n");
            print("     l'    \\ ,'._,\\ `.    .              /       ,--. l\n");
            print("  .,-        `._  |  |    |              \\       _   l .\n");
            print(" /              `\"--'    /              .'       ``. |  )\n");
            print(".\\    ,                 |                .        \\ `. '\n");
            print("`.                .     |                '._  __   ;. \\'\n");
            print("  `-..--------...'       \\                  `'  `-\"'.  \\\n");
            print("      `......___          `._                        |  \\\n");
            print("               /`            `..                     |   .\n");
            print("              /|                `-.                  |    L\n");
            print("             / |               \\   `._               .    |\n");
            print("           ,'  |,-\"-.   .       .     `.            /     |\n");
            print("         ,'    |     '   \\      |       `.         /      |\n");
            print("       ,'     /|       \\  .     |         .       /       |\n");
            print("     ,'      / |        \\  .    +          \\    ,'       .'\n");
            print("    .       .  |         \\ |     \\          \\_,'        / j\n");
            print("    |       |  L          `|      .          `        ,' '\n");
            print("    |    _. |   \\          /      |           .     .' ,'\n");
            print("    |   /  `|    \\        .       |  /        |   ,' .'\n");
            print("    |   ,-..\\     -.     ,        | /         |,.' ,'\n");
            print("    `. |___,`    /  `.   /`.       '          |  .'\n");
            print("      '-`-'     j     ` /.\"7-..../|          ,`-'\n");
            print("                |        .'  / _/_|          .\n");
            print("                `,       `\"'/\"'    \\          `.\n");
            print("                  `,       '.       `.         |\n");
            print("             __,.-'         `.        \\'       |\n");
            print("            /_,-'\\          ,'        |        _.\n");
            print("             |___.---.   ,-'        .-':,-\"`\\,' .\n");
            print("                  L,.--\"'           '-' |  ,' `-.\\\n");
            print("                                        `.' mh\n");
        elif pokemon_name == "Charizard":
            print("                 .\"-,.__\n");
            print("                 `.     `.  ,\n");
            print("              .--'  .._,'\"-' `.\n");
            print("             .    .'         `'\n");
            print("             `.   /          ,'\n");
            print("               `  '--.   ,-\"'\n");
            print("                `\"`   |  \\\n");
            print("                   -. \\, |\n");
            print("                    `--Y.'      ___.\n");
            print("                         \\     L._, \\\n");
            print("               _.,        `.   <  <\\                _\n");
            print("             ,' '           `, `.   | \\            ( `\n");
            print("          ../, `.            `  |    .\\`.           \\ \\_\n");
            print("         ,' ,..  .           _.,'    ||\\l            )  '\".\n");
            print("        , ,'   \\           ,'.-.`-._,'  |           .  _._`.\n");
            print("      ,' /      \\ \\        `' ' `--/   | \\          / /   ..\\\n");
            print("    .'  /        \\ .         |\\__ - _ ,'` `        / /     `.`.\n");
            print("    |  '          ..         `-...-\"  |  `-'      / /        . `.\n");
            print("    | /           |L__           |    |          / /          `. `.\n");
            print("   , /            .   .          |    |         / /             ` `\n");
            print("  / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \\\n");
            print(" / .           \\\"`_/. `-_ \\_,.  ,'    +-' `-'  _,        ..,-.    \\`.\n");
            print(".  '         .-f    ,'   `    '.       \\__.---'     _   .'   '     \\ \\\n");
            print("' /          `.'    l     .' /          \\..      ,_|/   `.  ,'`     L`\n");
            print("|'      _.-\"\"` `.    \\ _,'  `            \\ `.___`.'\"`-.  , |   |    | \\\n");
            print("||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|\n");
            print("||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||\n");
            print("|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||\n");
            print("||/            _,-------7 '              . |  `-'    l         /    `||\n");
            print(". |          ,' .-   ,' ||               | .-.        `.      .'     ||\n");
            print(" `'        ,'    `\".'    |               |    `.        '. -.'       `'\n");
            print("          /      ,'      |               |,'    \\-.._,.'/'\n");
            print("          .     /        .               .       \\    .''\n");
            print("        .`.    |         `.             /         :_,'.'\n");
            print("          \\ `...\\   _     ,'-.        .'         /_.-'\n");
            print("           `-.__ `,  `'   .  _.>----''.  _  __  /\n");
            print("                .'        /\"'          |  \"'   '_\n");
            print("               /_|.-'\\ ,\".             '.'`__'-( \\\n");
            print("                 / ,\"'\"\\,'               `/  `-.|\" mh\n");
        elif pokemon_name == "Squirtle":
            print("               _,........__\n");
            print("            ,-'            \"`-.\n");
            print("          ,'                   `-.\n");
            print("        ,'                        \\\n");
            print("      ,'                           .\n");
            print("      .'\\               ,\"\".       `\n");
            print("     ._.'|             / |  `       \\\n");
            print("     |   |            `-.'  ||       `.\n");
            print("     |   |            '-._,'||       | \\\n");
            print("     .`.,'             `..,'.'       , |`-.\n");
            print("     l                       .'`.  _/  |   `.\n");
            print("     `-.._'-   ,          _ _'   -\" \\  .     `\n");
            print("`.\"\"\"\"\"'-.`-...,---------','         `. `....__.\n");
            print(".'        `\"-..___      __,'\\          \\  \\     \\\n");
            print("\\_ .          |   `\"\"\"\"'    `.           . \\     \\\n");
            print("  `.          |              `.          |  .     L\n");
            print("    `.        |`--...________.'.        j   |     |\n");
            print("      `._    .'      |          `.     .|   ,     |\n");
            print("         `--,\\       .            `7\"\"' |  ,      |\n");
            print("            ` `      `            /     |  |      |    _,-'\"\"\"`-.\n");
            print("             \\ `.     .          /      |  '      |  ,'          `.\n");
            print("              \\  v.__  .        '       .   \\    /| /              \\\n");
            print("               \\/    `\"\"\\\"\"\"\"\"\"\"`.       \\   \\  /.''                |\n");
            print("                `        .        `._ ___,j.  `/ .-       ,---.     |\n");
            print("                ,`-.      \\         .\"     `.  |/        j     `    |\n");
            print("               /    `.     \\       /         \\ /         |     /    j\n");
            print("              |       `-.   7-.._ .          |\"          '         /\n");
            print("              |          `./_    `|          |            .     _,'\n");
            print("              `.           / `----|          |-............`---'\n");
            print("                \\          \\      |          |\n");
            print("               ,'           )     `.         |\n");
            print("                7____,,..--'      /          |\n");
            print("                                  `---.__,--.'mh\n");
        elif pokemon_name == "Wartortle":
            print("     __                                _.--'\"7\n");
            print("    `. `--._                        ,-'_,-  ,'\n");
            print("     ,'  `-.`-.                   /' .'    ,|\n");
            print("     `.     `. `-     __...___   /  /     - j\n");
            print("       `.     `  `.-\"\"        \" .  /       /\n");
            print("         \\     /                ` /       /\n");
            print("          \\   /                         ,'\n");
            print("          '._'_               ,-'       |\n");
            print("             | \\            ,|  |   ...-'\n");
            print("             || `         ,|_|  |   | `             _..__\n");
            print("            /|| |          | |  |   |  \\  _,_    .-\"     `-.\n");
            print("           | '.-'          |_|_,' __!  | /|  |  /           \\\n");
            print("   ,-...___ .=                  ._..'  /`.| ,`,.      _,.._ |\n");
            print("  |   |,.. \\     '  `'        ____,  ,' `--','  |    /      |\n");
            print(" ,`-..'  _)  .`-..___,---'_...._/  .'      '-...'   |      /\n");
            print("'.__' \"\"'      `.,------'\"'      ,/            ,     `.._.' `.\n");
            print("  `.             | `--........,-'.            .         \\     \\\n");
            print("    `-.          .   '.,--\"\"     |           ,'\\        |      .\n");
            print("       `.       /     |          L          ,\\  .       |  .,---.\n");
            print("         `._   '      |           \\        /  .  L      | /   __ `.\n");
            print("            `-.       |            `._   ,    l   .    j |   '  `. .\n");
            print("              |       |               `\"' |  .    |   /  '      .' |\n");
            print("              |       |                   j  |    |  /  , `.__,'   |\n");
            print("              `.      L                 _.   `    j ,'-'           |\n");
            print("               |`\"---..\\._______,...,--' |   |   /|'      /        j\n");
            print("               '       |                 |   .  / |      '        /\n");
            print("                .      .              ____L   \\'  j    -',       /\n");
            print("               / `.     .          _,\"     \\   | /  ,-','      ,'\n");
            print("              /    `.  ,'`-._     /         \\  i'.,'_,'      .'\n");
            print("             .       `.      `-..'             |_,-'      _.'\n");
            print("             |         `._      |            ''/      _,-'\n");
            print("             |            '-..._\\             `__,.--'\n");
            print("            ,'           ,' `-.._`.            .\n");
            print("           `.    __      |       \"'`.          |\n");
            print("             `-\"'  `\"\"\"\"'            7         `.\n");
            print("                                    `---'--.,'\"`' mh\n");
        elif pokemon_name == "Blastoise":
            print("                       _\n");
            print("            _,..-\"\"\"--' `,.-\".\n");
            print("          ,'      __.. --',  |\n");
            print("        _/   _.-\"' |    .' | |       ____\n");
            print("  ,.-\"\"'    `-\"+.._|     `.' | `-..,',--.`.\n");
            print(" |   ,.                      '    j 7    l \\__\n");
            print(" |.-'                            /| |    j||  .\n");
            print(" `.                   |         / L`.`\"\"','|\\  \\\n");
            print("   `.,----..._       ,'`\"'-.  ,'   \\ `\"\"'  | |  l\n");
            print("     Y        `-----'       v'    ,'`,.__..' |   .\n");
            print("      `.                   /     /   /     `.|   |\n");
            print("        `.                /     l   j       ,^.  |L\n");
            print("          `._            L       +. |._   .' \\|  | \\\n");
            print("            .`--...__,..-'\"\"'-._  l L  \"\"\"    |  |  \\\n");
            print("          .'  ,`-......L_       \\  \\ \\     _.'  ,'.  l\n");
            print("       ,-\"`. / ,-.---.'  `.      \\  L..--\"'  _.-^.|   l\n");
            print(" .-\"\".'\"`.  Y  `._'   '    `.     | | _,.--'\"     |   |\n");
            print("  `._'   |  |,-'|      l     `.   | |\"..          |   l\n");
            print("  ,'.    |  |`._'      |      `.  | |_,...---\"\"\"\"\"`    L\n");
            print(" /   |   j _|-' `.     L       | j ,|              |   |\n");
            print("`--,\"._,-+' /`---^..../._____,.L',' `.             |\\  |\n");
            print("   |,'      L                   |     `-.          | \\j\n");
            print("            .                    \\       `,        |  |\n");
            print("             \\                __`.Y._      -.     j   |\n");
            print("              \\           _.,'       `._     \\    |  j\n");
            print("              ,-\"`-----\"\"\"\"'           |`.    \\  7   |\n");
            print("             /  `.        '            |  \\    \\ /   |\n");
            print("            |     `      /             |   \\    Y    |\n");
            print("            |      \\    .             ,'    |   L_.-')\n");
            print("             L      `.  |            /      ]     _.-^._\n");
            print("              \\   ,'  `-7         ,-'      / |  ,'      `-._\n");
            print("             _,`._       `.   _,-'        ,',^.-            `.\n");
            print("          ,-'     v....  _.`\"',          _:'--....._______,.-'\n");
            print("        ._______./     /',,-'\"'`'--.  ,-'  `.\n");
            print("                 \"\"\"\"\"`.,'         _\\`----...' mh\n");
            print("                        --------\"\"'\n");
            print("\n");
            print("\n");
    elif choice=="4":
        print("You Quit :(")
        break
    if pokemon_level >=5:
        if pokemon_name=="Bulbasaur":
                pokemon_name="Ivysaur"
                print("Bulbasaur evolved into Ivysaur!\n")
        elif pokemon_name=="Charmander":
                pokemon_name="Charmeleon"
                print("Charmander evolved into Charmeleon!\n")
        elif pokemon_name=="Squirtle":
                pokemon_name="Wartortle"
                print("Squirtle evolved into Wartortle!\n")
    if pokemon_level >=10:
        if pokemon_name=="Ivysaur":
                pokemon_name="Venusaur"
                print("Ivysaur evolved into Venusaur!\n")
        elif pokemon_name=="Charmeleon":
                pokemon_name="Charizard"
                print("Charmeleon evolved into Charizard!\n")
        elif pokemon_name=="Wartortle":
                pokemon_name="Blastoise"
                print("Wartortle evolved into Blastoise!\n")
