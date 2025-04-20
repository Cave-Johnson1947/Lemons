import os
import pygame

pygame.init()
pygame.mixer.init()

# Debug: Check if set_window_position is available
print("Pygame version:", pygame.__version__)
print("Has set_window_position:", hasattr(pygame.display, 'set_window_position'))
# Window setup
WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 850
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Stephen Hawking Simulator")

# Colors
button_color = (255, 0, 0)  # Red
text_color = (0, 0, 0)  # Black
bg_color = (0, 0, 0)  # Black Background
scrollbar_color = (100, 100, 100)  # Gray
scrollbar_handle_color = (220, 220, 220)  # Brighter Gray for handle
highlight_color = (150, 150, 150)  # Grey for the oval highlight

button_width = 300
button_height = 100
corner_radius = 8  # Radius for rounded corners
font = pygame.font.SysFont(None, 40)

# Music folder
music_folder = r"C:\Users\Jacks\Downloads\meme"

# Define songs that should loop indefinitely
looping_songs = [
    "Portal Radio (Clean)",
    "Portal Radio (Radio Mix)",
    "Flint and Steel",
    "The Nether (Fast)",
    "Chicken Jockey",
    "Kirby",
    "I Am Steve",
    "Power Outage",
    "The Puppet",
    "FNAF 2 Ambience",
    "This is a Crafting Table",
    "Illuminati",
    "It's Been So Long",
    "Valve Theme",
    "As A Child I Yearned For The Mines",
    "Why You Should See The Minecraft Movie",
    "Steve's Lava Chicken",
    "The Nether (Normal)",
    "All Minecraft Memes",
    "Har-Har-Har-Har Meme",
    "FNAF Movie",
    "It's Been So Long",
    "I Am Placing Blocks And Shit",
    "End Credits",
    "Monday Left Me Broken",
    "Rule, Britannia!",
    "LET'S MINECRAFT",
    "NOT LIKE US-MINECRAFT",
    "FLINT AND MEAL",
    "NOT LIKE US-MINECRAFT FULL",
    "Lava Chicken (APT. Cover)",  
    "Ender Pearl",
    "COMING IN HOT",
    "FE!N x Steve (will change later)",
    "Minecraft Song",
    "Hot Lava And Chicken",
    "NEVER GONNA ENDER PEARL",
]

folders = {
    "GTA Sounds": {
        "songs": {
            "Yee Yee Ass Haircut": "yee-yee-ass-haircut-full.mp3",
            "San Andreas": "gta-san-andreas-abertura-oficial.mp3",
            "GTA V Death Sound": "gta-v-death-sound-effect-102.mp3",
            "Ni**a": "lamar_gtav_n___a_FFHFxBq.mp3",
            "Ah Shit": "gta-san-andreas-ah-shit-here-we-go-again_BWv0Gvc.mp3",
            "You Forget A Thousand Things Everyday": "gta-5-you-forget-a-thousand-things-everyday-1-audiotrimmer.mp3",
            "All We Have To Do Was Follow The Damm Train": "cj_1.mp3",
            "I'll Have Two Number 9's": "big-smoke-ill-have-two-number-9s-order.mp3",
        }
    },
    "Valve Sounds": {
        "subfolders": {
            "Half-Life": {
                "songs": {
                    "Don't Shoot Science": "dont-shoot-science-team-half-life-scientist.mp3",
                    "Half-Life Crowbar": "half-life-crowbar.mp3",
                    "Rise and Shine": "gman_rise_and_shine.mp3",
                    "Major Fracture Detected": "major-fracture-detected.mp3",
                    "Half-Life 2 Death": "half-life-2-death-sound.mp3",
                    "Valve Theme": "valve-theme-made-with-Voicemod.mp3",
                    "Acess Denied": "access-denied_Is238Ly.mp3",
                    "Who Ate All the Donuts": "half-life-donuts.mp3",
                    "Fascinating": "half-life-fascinating-made-with-Voicemod.mp3",
                    "Microwave": "half-life-microwave-made-with-Voicemod.mp3",
                    "AGH": "agh_uT05NZS.mp3",
                }
            },
            "Portal": {
                "songs": {
                    "Portal Radio (Clean)": "Portal Radio Ringtone Loop.mp3",
                    "Portal Radio (Radio Mix)": "4-01. Still Alive (Radio Mix).mp3",
                    "Wheatley Death": "Wheatley_bw_a4_death_trap01.wav",
                    "Are You Still There": "portal-turret-are-you-still-there_pGWToTI.mp3",
                    "Owowowow": "owowowow-made-with-Voicemod.mp3",
                    "Target Acquired": "target-acquired-made-with-Voicemod.mp3",
                    "There You Are": "there-you-are-made-with-Voicemod.mp3",
                    "Who Are You": "who-are-you-made-with-Voicemod.mp3",
                    "What Are You Doing": "what-are-you-doing-made-with-Voicemod.mp3",
                    "I AM NOT A MORON": "wheatly-i-am-not-a-moron-made-with-Voicemod.mp3",
                    "Cave Johnson Lemons": "cave-johnson-lemons-full.mp3",
                    "Because I'm a Potato": "because-im-a-potato-101soundboards.mp3",
                    "SPAAAAAAAAAAACE": "space-core-made-with-Voicemod.mp3",
                    "Still Alive": "Still Alive.mp3",
                    "Still Alive (1950's)": "Still Alive (From _Portal_) 4.mp3",
                    "Want You Gone": "3-13 - Want You Gone [Feat. Ellen McLain].mp3",
                    "Want You Gone (1950's)": "Want You Gone - Frank Sinatra Big Band Swing Version (The 8-Bit Big Band) 4.mp3",
                    "Portal Gun": "portal-gun-ice.mp3",
                    "You Have Brain Damage": "you-have-brain-damage-made-with-Voicemod.mp3",
                    "Cave Johnson Multiverse": "Portal 2 Perpetual Testing Initiative (mp3cut.net).mp3",
                    "Cave Johnson Methods": "Portal 2 Perpetual Testing Initiative (mp3cut.net) (1).mp3",
                }
            }
        }
    },
    "Meme Sounds": {
        "songs": {
            "Vine Boom": "vine-boom-sound-effect_KT89XIq.mp3",
            "Communist Detected": "communist-detected-on-american-soil-lethal-force-engaged.mp3",
            "Get Out": "tuco-get-out.mp3",
            "Metal Pipe": "jixaw-metal-pipe-falling-sound.mp3",
            "Bill Nye": "af72d5da-ca12-4c9d-8b1a-c6833c517314.mp3",
            "Pacer Test": "fitnessgram-pacer-test-loud.mp3",
            "Limit On Talking": "limit-on-talking.mp3",
            "Long Before Time Had A Name": "long-before-time-had-a-name-made-with-Voicemod.mp3",
            "Dial Up Internet": "Dial Up Internet - Sound Effect (HD).mp3",
            "Are You Sure": "omni-man-are-you-sure.mp3",
            "I Am The Alpha": "I AM THE ALPHA  Christian Edit   #JesusChrist #Christianity #Revelation.mp3",
            "My Mommy Said No More Skibidi Toilet": "my-mommy-said-no-more-skibidi-toilet-made-with-Voicemod.mp3",
            "AAAAAAAAAAAAAA": "aaaaaaaa-online-audio-converter_r9waVUO.mp3",
            "I May Not Have A Brain": "i-may-not-have-a-brain-gentleman-made-with-Voicemod.mp3",
            "You Know What Else Is Massive": "you-know-what-else-is-massive-made-with-Voicemod.mp3",
            "Me After Fixing My 3D Printer": "the-greatest-technician-that's-ever-lived-made-with-Voicemod.mp3",
            "Agua Means Water": "Spy Kids 3 is a CGI Fever Dream-[AudioTrimmer.com].mp3",
            "Mario Death": "super-mario-death-sound-sound-effect.mp3",
            "Wow That's A Lot Of Words": "duke-nukem-wow-thats-a-lot-of-words.mp3",
            "Vsauce Intro": "jake-chudnow-edited_y1t8j5q.mp3",
        }
    },
    "Music": {
        "songs": {
            "Rap God": "Eminem - Rap God (Fast part).mp3",
            "Eminem Rap": "my-name-is-eminem-and-i-like-to-rap.mp3",
            "Guess Whos Back": "guess-whos-back-shadys-back.mp3",
            "Oranana": "Voicy_Eminem Rhymes Banana And Orange Oranana.mp3",
            "Criminal": "im-a-criminal.mp3",
            "Erika Song": "Erika-German-Song-Sound-Effect.mp3",
            "USSR": "Soviet-Union-Anthem-Sound-Effect.mp3",
            "Kirby": "KIRBY DREAM LAND - AUDIO FROM JAYUZUMI.COM.mp3",
            "Never Gonna Give You Down": "Rick Astley - Never Gonna Give You Up (Official Music Video).mp3",
            "Rule, Britannia!": "Rule, Britannia! (Instrumental).mp3",
            "Moskau": "Dschinghis Khan - Moskau (Starparade 14.06.1979).mp3",
            "Monday Left Me Broken": "monday-left-me-broken-cat-made-with-Voicemod.mp3",
            "Saul Goodman": "saul-goodman-made-with-Voicemod.mp3",
            "Free Bird": "only-the-best-part-of-free-bird-made-with-Voicemod.mp3",
            "I Am Iron Man": "i-am-iron-man-(epic-music-plays)-made-with-Voicemod.mp3",
            "JESUS": "jesus-christ-made-with-Voicemod.mp3",
            "Rapping For Jesus": "Jesus Christ is my nigga (Lyrics).mp3",
            "Lord I Need You Now": "Which type of reader are you_  @BibleWithDaniel #shorts #viral #christian #jesus.mp3",
            "Pirate Raido": "pirate-with-radio-made-with-Voicemod.mp3",
            "You Are A Pirate":"Lazy Town  You Are A Pirate Music Video.mp3",
            "31 Words That Sound Like Slurs But Aren't (Full)": "31 Words That Sound Like Slurs But Aren't-[AudioTrimmer.com]n.mp3",
            "31 Words That Sound Like Slurs But Aren't (NIG-)": "31 Words That Sound Like Slurs But Aren't-[AudioTrimmer.com]-[AudioTrimmer.com]-[AudioTrimmer.com].mp3",
            "Colonization Be Like": "Stereotypical Music across the World-[AudioTrimmer.com].mp3",
            "Level 1-1": "Super Mario Brothers 1 Music - Main Theme & Overworld.mp3",
            "Bad To The Bone": "bad-to-the-bone-full-made-with-Voicemod.mp3",
            "Oiia Oiia Cat": "OIIAOIIA CAT but in 4K.mp3"
        }
    },
    "Game Sounds": {
        "subfolders": {
            "FNAF": {
                "songs": {
                    "Michael NO": "michael-dont-leave-me-here.mp3",
                    "I Always Come Back": "ialwayscomeback.mp3",
                    "Power Outage": "Five-Nights-at-Freddys-Toreador-March-Sound-Effect.mp3",
                    "The Puppet": "Voicy_Fnaf 2 music box.mp3",
                    "FNAF 2 Ambience": "Voicy_Fnaf 2 ambience.mp3",
                    "Springlock Failure": "springlocked-(william-afton-death)-[fnaf-sfm]-made-with-Voicemod.mp3",
                    "My Name is Edwin": "my-name-is-edwin-i-made-the-mimic-made-with-Voicemod.mp3",
                    "Join Us For A Bite": "The Living Tombstone - Join Us for a Bite Remix.mp3",
                    "FNAF 1 Jumpscare": "fnaf-1-jumpscare-sound-made-with-Voicemod.mp3",
                    "FNAF 2 Jumpscare": "fnaf-2-jumpscare-sound-effect-made-with-Voicemod.mp3",
                    "FNAF 3 Jumpscare": "fnaf-3-jumpscare-sound-made-with-Voicemod.mp3",
                    "FNAF 4 Jumpscare": "fnaf-4-jumpscare-sound-effect-made-with-Voicemod.mp3",
                    "FNAF SL Jumpscare": "fnaf-sl_-jumpscare-sound_-funtime-freddy-made-with-Voicemod.mp3",
                    "FNAF 6 Jumpscare": "fnaf-6-jumpscare-made-with-Voicemod.mp3",
                    "FNAF 6 Ending": "fnaf-6-ending.mp3",
                    "It's Been So Long": "it's-been-so-long-made-with-Voicemod.mp3",
                    "Har-Har-Har-Har Meme": "har-har-har-har-fnaf-abdul-cisse-tiktok-(1)-made-with-Voicemod.mp3",
                    "FNAF Movie": "FNAF MOVIE _ Toreador March song (stem separation) 4.mp3",
                    "FNAF Brain Rot": "ytmp3free.cc_springtrap-uses-genalpha-slang-youtubemp3free.org - Copy.mp3",
                    "Toreadors March": "toreadors-march-made-with-Voicemod.mp3",
                    "Stuck Inside": "stuck-inside-part-6-(last-part)-made-with-Voicemod.mp3",
                    "See That Meme Up There Sportsy": "m2-res_360p.mp3",
                    "William Afton's Speech": "FNAF William Afton's (Springtrap) speech - I hate you. I've ALWAYS hated you.mp3",
                    "Hello Internet, Welcome to Game Theory!": "HELLO INTERNET, WELCOME TO GAME THEORY!.mp3",
                    "Intro to Game Theory": "matpat-intro.-made-with-Voicemod.mp3",
                    "But Hey, That's Just A Theory": "but-hey,-that's-just-a-theory,-a-game-theory!-(sans-is-ness)-made-with-Voicemod.mp3",
                    "Phone Guy": "PHONE GUY IS FED UP WITH MATPAT! (FNAF ANIMATIC).mp3",
                    "Phone Guy (FNAF 1 Night 1)":"Fnaf 1 Night 1 Call.mp3",
                    "Animatronics Do Get A Bit Quirky At Night": "quirky-at-night.mp3",
                    "Jackie's Box": "JACKIE'S BOX - FNAF MIMIC SONG (Secret Of The Mimic Original Song).mp3",
                    "WAS THAT THE BITE OF 87": "was-that-the-bite-of-87-made-with-Voicemod.mp3",
                    "Freddy's Honk": "fnaf-12-3-freddys-nose-sound.mp3",
                    "Withered Bonnie Gets Revenge": "Withered bonnie gets revenge.mp3",
                    "Fredbear Plush": "Who you gonna call_.mp3",
                }
            },
            "Minecraft": {
                "songs": {
                    "Flint and Steel": "1_HOUR_of_FLINT_AND_STEEL_Mincraft_Movie_Trailer (1) - Copy.mp3",
                    "The Nether (Fast)": "the-nether-made-with-Voicemod.mp3",
                    "The Nether (Normal)": "1_HOUR_of_THE_NETHER_Mincraft_Movie_Trailer.mp3",
                    "Chicken Jockey": "chicken-jockey-minecraft-movie-made-with-Voicemod.mp3",
                    "I Am Steve": "i...-am-steve-made-with-Voicemod.mp3",
                    "This is a Crafting Table": "CRAFTING TABLE Minecraft Movie Meme Sound - NO COPYRIGHT (HD)-[AudioTrimmer.com].mp3",
                    "As A Child I Yearned For The Mines": "as-a-child-i-yearned-for-the-mines.mp3",
                    "Steve's Lava Chicken":  "Steve's Lava Chicken.mp3", 
                    "Why You Should See The Minecraft Movie": "Why you should see the minecraft movie.mp3",
                    "I Am Placing Blocks And Shit": "Jack_black_unreleased_Minecraft_song (1).mp3",
                    "End Credits": "Steve's Last Song - A Minecraft Movie [Jack Black A.I].mp3",
                    "LET'S MINECRAFT": "LET'S MINECRAFT  #minecraft #minecraftmemes #edit #trend.mp3",
                    "NOT LIKE US-MINECRAFT": "I AM STEVE 🗣️🗣️🔥🔥  #minecraft   #minecraftmeme   #edit   #trend   #song 4.mp3",
                    "NOT LIKE US-MINECRAFT FULL": "Not Like Steve (Audio).mp3",
                    "Lava Chicken (APT. Cover)": "Lava Chicken (Audio).mp3", 
                    "FE!N x Steve (will change later)": "FE!N x Steve (ins. @doombreaker4689) #minecraft #minecraftmeme #edit #song #trend.mp3",
                    "Ender Pearl": "ender-pearl-made-with-Voicemod.mp3",
                    "COMING IN HOT": "10 MINUTES of COMING IN HOTMincraft Movie Trailer.mp3",
                    "Minecraft Song": "C418 - Minecraft - Minecraft Volume Alpha.mp3",
                    "FLINT AND MEAL": "Snapchat-1976634028.mp3",
                    "Hot Lava And Chicken": "Minecraft Hot Lava And Chicken.mp3",
                    "NEVER GONNA ENDER PEARL": "NEVER GONNA ENDER PEARL (scrapped).mp3",
                    "All Minecraft Memes": "videoplayback.mp3",
                }
            }
        }
    }
}

# Function to collect all songs from folders and subfolders
def collect_all_songs(folders):
    all_songs = {}
    for folder_name, folder_data in folders.items():
        if "songs" in folder_data:
            # Top-level folder with songs
            for song_name, file_name in folder_data["songs"].items():
                # Avoid duplicates by appending folder name to song name if necessary
                display_name = song_name
                counter = 1
                while display_name in all_songs:
                    display_name = f"{song_name} ({folder_name} {counter})"
                    counter += 1
                all_songs[display_name] = file_name
        elif "subfolders" in folder_data:
            # Folder with subfolders
            for subfolder_name, subfolder_data in folder_data["subfolders"].items():
                for song_name, file_name in subfolder_data["songs"].items():
                    # Avoid duplicates by appending subfolder name to song name
                    display_name = song_name
                    counter = 1
                    while display_name in all_songs:
                        display_name = f"{song_name} ({subfolder_name} {counter})"
                        counter += 1
                    all_songs[display_name] = file_name
    return all_songs

# Add "All Songs" folder with dynamically collected songs
folders["All Songs"] = {
    "songs": collect_all_songs(folders)
}

# Helper function to wrap text and render it within the button
def render_wrapped_text(text, font, text_color, max_width, button_rect):
    words = text.split(" ")
    lines = []
    current_line = []
    current_width = 0

    # Split text into lines that fit within max_width
    for word in words:
        test_line = " ".join(current_line + [word])
        text_surface = font.render(test_line, True, text_color)
        if text_surface.get_width() <= max_width:
            current_line.append(word)
            current_width = text_surface.get_width()
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
            current_width = font.render(word, True, text_color).get_width()
    if current_line:
        lines.append(" ".join(current_line))

    # Render each line and center them vertically and horizontally
    rendered_lines = [font.render(line, True, text_color) for line in lines]
    total_height = sum(line.get_height() for line in rendered_lines)
    # Add a vertical offset to nudge the text downward for better visual centering
    vertical_offset = 10  # Adjust this value if needed
    y_offset = button_rect.centery - total_height // 2 + vertical_offset

    for line_surface in rendered_lines:
        line_rect = line_surface.get_rect(centery=y_offset, centerx=button_rect.centerx)
        screen.blit(line_surface, line_rect)
        y_offset += line_surface.get_height()

# UI elements
current_folder = None  # Top-level folder (e.g., "Game Sounds")
current_subfolder = None  # Subfolder (e.g., "Minecraft")
dragging = False
mouse_offset = (0, 0)
scroll_offset = 0  # Horizontal scroll offset
scrollbar_dragging = False
scrollbar_pos = 0  # Position of scrollbar handle
is_paused = False  # Track whether music is paused

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                if current_folder is None:
                    # Main menu: Show top-level folders
                    max_items_in_column = 5
                    column_x = 50
                    column_width = 350
                    for i, folder in enumerate(folders):
                        column_index = i // max_items_in_column
                        row_index = i % max_items_in_column
                        folder_rect = pygame.Rect(column_x + column_index * column_width, 100 + row_index * (button_height + 20), button_width, button_height)
                        if folder_rect.collidepoint(event.pos):
                            current_folder = folder
                            scroll_offset = 0  # Reset scroll
                            scrollbar_pos = 0  # Reset scrollbar position
                            break
                elif current_folder and current_subfolder is None:
                    # Subfolder menu: Show subfolders (e.g., "Minecraft", "FNAF")
                    if "subfolders" in folders[current_folder]:
                        subfolders = folders[current_folder]["subfolders"]
                        max_items_in_column = 5
                        column_x = 50 - scroll_offset
                        column_width = 350
                        total_items = len(subfolders) + 1  # Include only Back button
                        for i in range(total_items):
                            column_index = i // max_items_in_column
                            row_index = i % max_items_in_column
                            if i < len(subfolders):
                                # Subfolder button
                                subfolder = list(subfolders.keys())[i]
                                subfolder_rect = pygame.Rect(column_x + column_index * column_width, 100 + row_index * (button_height + 20), button_width, button_height)
                                if subfolder_rect.collidepoint(event.pos):
                                    current_subfolder = subfolder
                                    scroll_offset = 0  # Reset scroll
                                    scrollbar_pos = 0  # Reset scrollbar position
                                    break
                            else:
                                # Back button
                                back_button = pygame.Rect(column_x + column_index * column_width, 100 + row_index * (button_height + 20), button_width, button_height)
                                if back_button.collidepoint(event.pos):
                                    current_folder = None
                                    scroll_offset = 0  # Reset scroll
                                    scrollbar_pos = 0  # Reset scrollbar position
                                    break
                        # Scrollbar click detection
                        scrollbar_rect = pygame.Rect(50, WINDOW_HEIGHT - 70, WINDOW_WIDTH - 100, 20)
                        if scrollbar_rect.collidepoint(event.pos):
                            scrollbar_dragging = True
                            scrollbar_pos = max(0, min(event.pos[0] - 50, WINDOW_WIDTH - 100 - 50))
                    else:
                        # No subfolders, go straight to songs
                        folder_songs = list(folders[current_folder]["songs"].items())
                        max_items_in_column = 5
                        column_x = 50 - scroll_offset
                        column_width = 350
                        total_items = len(folder_songs) + 3  # Include Pause, Stop, and Back buttons
                        for i in range(total_items):
                            column_index = i // max_items_in_column
                            row_index = i % max_items_in_column
                            if i < len(folder_songs):
                                # Song button
                                song_name, file_name = folder_songs[i]
                                song_rect = pygame.Rect(column_x + column_index * column_width, 100 + row_index * (button_height + 20), button_width, button_height)
                                if song_rect.collidepoint(event.pos):
                                    song_path = os.path.join(music_folder, file_name)
                                    print(f"Attempting to play: {song_path}")
                                    if os.path.exists(song_path):
                                        pygame.mixer.music.load(song_path)
                                        if song_name in looping_songs:
                                            pygame.mixer.music.play(loops=-1)  # Loop indefinitely
                                        else:
                                            pygame.mixer.music.play(loops=0)  # Play once
                                        is_paused = False  # Reset pause state when playing new song
                                    else:
                                        print(f"Error: File not found at {song_path}")
                                    break
                            elif i == len(folder_songs):
                                # Pause button
                                pause_button = pygame.Rect(column_x + column_index * column_width, 100 + row_index * (button_height + 20), button_width, button_height)
                                if pause_button.collidepoint(event.pos):
                                    if is_paused:
                                        pygame.mixer.music.unpause()
                                        is_paused = False
                                        print("Music resumed")
                                    else:
                                        pygame.mixer.music.pause()
                                        is_paused = True
                                        print("Music paused")
                                    break
                            elif i == len(folder_songs) + 1:
                                # Stop button
                                stop_button = pygame.Rect(column_x + column_index * column_width, 100 + row_index * (button_height + 20), button_width, button_height)
                                if stop_button.collidepoint(event.pos):
                                    pygame.mixer.music.stop()
                                    is_paused = False  # Reset pause state
                                    print("Music stopped")
                                    break
                            else:
                                # Back button
                                back_button = pygame.Rect(column_x + column_index * column_width, 100 + row_index * (button_height + 20), button_width, button_height)
                                if back_button.collidepoint(event.pos):
                                    current_folder = None
                                    scroll_offset = 0  # Reset scroll
                                    scrollbar_pos = 0  # Reset scrollbar position
                                    break
                        # Scrollbar click detection
                        scrollbar_rect = pygame.Rect(50, WINDOW_HEIGHT - 70, WINDOW_WIDTH - 100, 20)
                        if scrollbar_rect.collidepoint(event.pos):
                            scrollbar_dragging = True
                            scrollbar_pos = max(0, min(event.pos[0] - 50, WINDOW_WIDTH - 100 - 50))
                else:
                    # Song menu: Show songs in the subfolder
                    folder_songs = list(folders[current_folder]["subfolders"][current_subfolder]["songs"].items())
                    max_items_in_column = 5
                    column_x = 50 - scroll_offset
                    column_width = 350
                    total_items = len(folder_songs) + 3  # Include Pause, Stop, and Back buttons
                    for i in range(total_items):
                        column_index = i // max_items_in_column
                        row_index = i % max_items_in_column
                        if i < len(folder_songs):
                            # Song button
                            song_name, file_name = folder_songs[i]
                            song_rect = pygame.Rect(column_x + column_index * column_width, 100 + row_index * (button_height + 20), button_width, button_height)
                            if song_rect.collidepoint(event.pos):
                                song_path = os.path.join(music_folder, file_name)
                                print(f"Attempting to play: {song_path}")
                                if os.path.exists(song_path):
                                    pygame.mixer.music.load(song_path)
                                    if song_name in looping_songs:
                                        pygame.mixer.music.play(loops=-1)  # Loop indefinitely
                                    else:
                                        pygame.mixer.music.play(loops=0)  # Play once
                                    is_paused = False  # Reset pause state when playing new song
                                else:
                                    print(f"Error: File not found at {song_path}")
                                break
                        elif i == len(folder_songs):
                            # Pause button
                            pause_button = pygame.Rect(column_x + column_index * column_width, 100 + row_index * (button_height + 20), button_width, button_height)
                            if pause_button.collidepoint(event.pos):
                                if is_paused:
                                    pygame.mixer.music.unpause()
                                    is_paused = False
                                    print("Music resumed")
                                else:
                                    pygame.mixer.music.pause()
                                    is_paused = True
                                    print("Music paused")
                                break
                        elif i == len(folder_songs) + 1:
                            # Stop button
                            stop_button = pygame.Rect(column_x + column_index * column_width, 100 + row_index * (button_height + 20), button_width, button_height)
                            if stop_button.collidepoint(event.pos):
                                pygame.mixer.music.stop()
                                is_paused = False  # Reset pause state
                                print("Music stopped")
                                break
                        else:
                            # Back button
                            back_button = pygame.Rect(column_x + column_index * column_width, 100 + row_index * (button_height + 20), button_width, button_height)
                            if back_button.collidepoint(event.pos):
                                current_subfolder = None
                                scroll_offset = 0  # Reset scroll when going back to subfolder menu
                                scrollbar_pos = 0  # Reset scrollbar position
                                break
                    # Scrollbar click detection
                    scrollbar_rect = pygame.Rect(50, WINDOW_HEIGHT - 70, WINDOW_WIDTH - 100, 20)
                    if scrollbar_rect.collidepoint(event.pos):
                        scrollbar_dragging = True
                        scrollbar_pos = max(0, min(event.pos[0] - 50, WINDOW_WIDTH - 100 - 50))
            elif event.button == 3:  # Right-click to drag window
                dragging = True
                mouse_offset = (event.pos[0] - screen.get_rect().x, event.pos[1] - screen.get_rect().y)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                scrollbar_dragging = False
            elif event.button == 3:
                dragging = False

        if event.type == pygame.MOUSEMOTION:
            if dragging:
                new_pos = (event.pos[0] - mouse_offset[0], event.pos[1] - mouse_offset[1])
                pygame.display.set_window_position(new_pos)
            elif scrollbar_dragging:
                scrollbar_pos = max(0, min(event.pos[0] - 50, WINDOW_WIDTH - 100 - 50))
                if current_subfolder:
                    total_content_width = ((len(folders[current_folder]["subfolders"][current_subfolder]["songs"]) + 3) // 5 + 1) * 350
                elif "subfolders" in folders[current_folder]:
                    total_content_width = ((len(folders[current_folder]["subfolders"]) + 1) // 5 + 1) * 350
                else:
                    total_content_width = ((len(folders[current_folder]["songs"]) + 3) // 5 + 1) * 350
                visible_width = WINDOW_WIDTH - 100
                if total_content_width > visible_width:
                    scroll_offset = (scrollbar_pos / (WINDOW_WIDTH - 150)) * (total_content_width - visible_width)

        # Esc key functionality for navigation
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Esc to go back
                if current_subfolder:  # If in a subfolder (e.g., "Valve Songs" > "Half-Life")
                    current_subfolder = None
                    scroll_offset = 0  # Reset scroll
                    scrollbar_pos = 0  # Reset scrollbar position
                elif current_folder:  # If in a folder (e.g., "Valve Songs")
                    current_folder = None
                    scroll_offset = 0  # Reset scroll
                    scrollbar_pos = 0  # Reset scrollbar position
                # If already in the main menu, reset state
                else:
                    current_folder = None
                    current_subfolder = None
                    scroll_offset = 0  # Reset scroll
                    scrollbar_pos = 0  # Reset scrollbar position

    # Draw UI
    if current_folder is None:
        # Main menu: Show top-level folders
        max_items_in_column = 5
        column_x = 50
        column_width = 350
        for i, folder in enumerate(folders):
            column_index = i // max_items_in_column
            row_index = i % max_items_in_column
            folder_rect = pygame.Rect(column_x + column_index * column_width, 100 + row_index * (button_height + 20), button_width, button_height)
            # Draw red box with rounded corners (no border)
            pygame.draw.rect(screen, button_color, folder_rect, border_radius=corner_radius)
            # Use wrapped text rendering
            render_wrapped_text(folder, font, text_color, button_width - 20, folder_rect)  # Subtract 20 for padding

    elif current_folder and current_subfolder is None:
        # Subfolder menu: Show subfolders or songs
        if "subfolders" in folders[current_folder]:
            subfolders = folders[current_folder]["subfolders"]
            max_items_in_column = 5
            column_x = 50 - scroll_offset
            column_width = 350
            total_items = len(subfolders) + 1  # Include only Back button
            for i in range(total_items):
                column_index = i // max_items_in_column
                row_index = i % max_items_in_column
                button_rect = pygame.Rect(column_x + column_index * column_width, 100 + row_index * (button_height + 20), button_width, button_height)
                if button_rect.x + button_width > 50 and button_rect.x < WINDOW_WIDTH - 50:
                    pygame.draw.rect(screen, button_color, button_rect, border_radius=corner_radius)
                    if i < len(subfolders):
                        # Subfolder button
                        subfolder = list(subfolders.keys())[i]
                        render_wrapped_text(subfolder, font, text_color, button_width - 20, button_rect)
                    else:
                        # Back button
                        render_wrapped_text("Back", font, text_color, button_width - 20, button_rect)
            # Scrollbar for subfolders
            total_content_width = (total_items // max_items_in_column + 1) * column_width
            visible_width = WINDOW_WIDTH - 100
            if total_content_width > visible_width:
                scrollbar_rect = pygame.Rect(50, WINDOW_HEIGHT - 70, WINDOW_WIDTH - 100, 20)
                pygame.draw.rect(screen, scrollbar_color, scrollbar_rect, border_radius=corner_radius)
                handle_width = max(50, (visible_width / total_content_width) * (WINDOW_WIDTH - 100))
                handle_x = 50 + scrollbar_pos
                handle_rect = pygame.Rect(handle_x, WINDOW_HEIGHT - 70, handle_width, 20)
                pygame.draw.rect(screen, scrollbar_handle_color, handle_rect, border_radius=corner_radius)
        else:
            # No subfolders, show songs directly
            folder_songs = list(folders[current_folder]["songs"].items())
            max_items_in_column = 5
            column_x = 50 - scroll_offset
            column_width = 350
            total_items = len(folder_songs) + 3  # Include Pause, Stop, and Back buttons
            for i in range(total_items):
                column_index = i // max_items_in_column
                row_index = i % max_items_in_column
                button_rect = pygame.Rect(column_x + column_index * column_width, 100 + row_index * (button_height + 20), button_width, button_height)
                if button_rect.x + button_width > 50 and button_rect.x < WINDOW_WIDTH - 50:
                    pygame.draw.rect(screen, button_color, button_rect, border_radius=corner_radius)
                    if i < len(folder_songs): # Song button
                        song_name, _ = folder_songs[i]
                        # Draw a grey oval around "My Name is Edwin" in All Songs
                        if current_folder == "All Songs" and song_name == "My Name is Edwin":
                            oval_rect = button_rect.inflate(20, 10)
                            pygame.draw.ellipse(screen, highlight_color, oval_rect, 3)
                        render_wrapped_text(song_name, font, text_color, button_width - 20, button_rect)
                    elif i == len(folder_songs):
                        # Pause button
                        render_wrapped_text("Resume" if is_paused else "Pause", font, text_color, button_width - 20, button_rect)
                    elif i == len(folder_songs) + 1:
                        # Stop button
                        render_wrapped_text("Stop", font, text_color, button_width - 20, button_rect)
                    else:
                        # Back button
                        render_wrapped_text("Back", font, text_color, button_width - 20, button_rect)
            # Scrollbar
            total_content_width = (total_items // max_items_in_column + 1) * column_width
            visible_width = WINDOW_WIDTH - 100
            if total_content_width > visible_width:
                scrollbar_rect = pygame.Rect(50, WINDOW_HEIGHT - 70, WINDOW_WIDTH - 100, 20)
                pygame.draw.rect(screen, scrollbar_color, scrollbar_rect, border_radius=corner_radius)
                handle_width = max(50, (visible_width / total_content_width) * (WINDOW_WIDTH - 100))
                handle_x = 50 + scrollbar_pos
                handle_rect = pygame.Rect(handle_x, WINDOW_HEIGHT - 70, handle_width, 20)
                pygame.draw.rect(screen, scrollbar_handle_color, handle_rect, border_radius=corner_radius)

    else:
        # Song menu: Show songs in the subfolder
        folder_songs = list(folders[current_folder]["subfolders"][current_subfolder]["songs"].items())
        max_items_in_column = 5
        column_x = 50 - scroll_offset
        column_width = 350
        total_items = len(folder_songs) + 3  # Include Pause, Stop, and Back buttons
        for i in range(total_items):
            column_index = i // max_items_in_column
            row_index = i % max_items_in_column
            button_rect = pygame.Rect(column_x + column_index * column_width, 100 + row_index * (button_height + 20), button_width, button_height)
            if button_rect.x + button_width > 50 and button_rect.x < WINDOW_WIDTH - 50:
                # Draw the button
                pygame.draw.rect(screen, button_color, button_rect, border_radius=corner_radius)
                if i < len(folder_songs):
                    # Song button
                    song_name, _ = folder_songs[i]
                    # Draw a grey oval around "My Name is Edwin" in FNAF
                    if current_folder == "Game Sounds" and current_subfolder == "FNAF" and song_name == "My Name is Edwin":
                        # Define the oval rect (slightly larger than the button)
                        oval_rect = button_rect.inflate(20, 10)  # Increase width by 20, height by 10 for oval shape
                        pygame.draw.ellipse(screen, highlight_color, oval_rect, 3)  # Draw oval with 3px thickness
                    render_wrapped_text(song_name, font, text_color, button_width - 20, button_rect)
                elif i == len(folder_songs):
                    # Pause button
                    render_wrapped_text("Resume" if is_paused else "Pause", font, text_color, button_width - 20, button_rect)
                elif i == len(folder_songs) + 1:
                    # Stop button
                    render_wrapped_text("Stop", font, text_color, button_width - 20, button_rect)
                else:
                    # Back button
                    render_wrapped_text("Back", font, text_color, button_width - 20, button_rect)
        # Scrollbar
        total_content_width = (total_items // max_items_in_column + 1) * column_width
        visible_width = WINDOW_WIDTH - 100
        if total_content_width > visible_width:
            scrollbar_rect = pygame.Rect(50, WINDOW_HEIGHT - 70, WINDOW_WIDTH - 100, 20)
            pygame.draw.rect(screen, scrollbar_color, scrollbar_rect, border_radius=corner_radius)
            handle_width = max(50, (visible_width / total_content_width) * (WINDOW_WIDTH - 100))
            handle_x = 50 + scrollbar_pos
            handle_rect = pygame.Rect(handle_x, WINDOW_HEIGHT - 70, handle_width, 20)
            pygame.draw.rect(screen, scrollbar_handle_color, handle_rect, border_radius=corner_radius)

    pygame.display.flip()
    clock.tick(30)
pygame.quit()