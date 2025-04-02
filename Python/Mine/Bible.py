import random

bible_quotes = {
    "sad": [
        "The Lord is near to the brokenhearted and saves the crushed in spirit. – Psalm 34:18",
        "Cast your burden on the Lord, and he will sustain you. – Psalm 55:22",
        "I have told you these things, so that in me you may have peace. In this world you will have trouble. But take heart! I have overcome the world. – John 16:33",
        "He heals the brokenhearted and binds up their wounds. – Psalm 147:3",
        "Blessed are those who mourn, for they shall be comforted. – Matthew 5:4",
        "Weeping may tarry for the night, but joy comes with the morning. – Psalm 30:5",
        "The Lord is good, a stronghold in the day of trouble; he knows those who take refuge in him. – Nahum 1:7",
        "My comfort in my suffering is this: Your promise preserves my life. – Psalm 119:50",
        "Though I walk through the valley of the shadow of death, I will fear no evil, for you are with me. – Psalm 23:4",
        "He will wipe away every tear from their eyes. – Revelation 21:4",
        "The Lord is my rock, my fortress and my deliverer. – Psalm 18:2",
        "When the righteous cry for help, the Lord hears and delivers them out of all their troubles. – Psalm 34:17",
        "Even though I walk through the darkest valley, I will fear no evil, for you are with me. – Psalm 23:4",
        "The Lord is a refuge for the oppressed, a stronghold in times of trouble. – Psalm 9:9",
        "Those who sow in tears shall reap with shouts of joy! – Psalm 126:5"
    ],
    "happy": [
        "The joy of the Lord is your strength. – Nehemiah 8:10",
        "Rejoice in the Lord always; again I will say, Rejoice. – Philippians 4:4",
        "Every good gift and every perfect gift is from above. – James 1:17",
        "This is the day that the Lord has made; let us rejoice and be glad in it. – Psalm 118:24",
        "You make known to me the path of life; in your presence there is fullness of joy. – Psalm 16:11",
        "A cheerful heart is good medicine, but a crushed spirit dries up the bones. – Proverbs 17:22",
        "Shout for joy to the Lord, all the earth. – Psalm 100:1",
        "I will be glad and rejoice in your love, for you saw my affliction and knew the anguish of my soul. – Psalm 31:7",
        "The hope of the righteous brings joy, but the expectation of the wicked comes to nothing. – Proverbs 10:28",
        "You have turned my mourning into dancing; you have removed my sackcloth and clothed me with joy. – Psalm 30:11",
        "Rejoice always, pray continually, give thanks in all circumstances. – 1 Thessalonians 5:16-18",
        "May your fountain be blessed, and may you rejoice in the wife of your youth. – Proverbs 5:18",
        "The precepts of the Lord are right, giving joy to the heart. – Psalm 19:8",
        "I have set the Lord always before me; because he is at my right hand, I shall not be shaken. – Psalm 16:8",
        "Blessed are the people whose God is the Lord! – Psalm 144:15"
    ],
    "peace": [
        "Peace I leave with you; my peace I give you. – John 14:27",
        "And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus. – Philippians 4:7",
        "You will keep in perfect peace those whose minds are steadfast because they trust in you. – Isaiah 26:3",
        "Great peace have those who love your law, and nothing can make them stumble. – Psalm 119:165",
        "The Lord gives strength to his people; the Lord blesses his people with peace. – Psalm 29:11",
        "Come to me, all you who are weary and burdened, and I will give you rest. – Matthew 11:28",
        "Turn from evil and do good; seek peace and pursue it. – Psalm 34:14",
        "The fruit of that righteousness will be peace; its effect will be quietness and confidence forever. – Isaiah 32:17",
        "Let the peace of Christ rule in your hearts, since as members of one body you were called to peace. – Colossians 3:15",
        "He makes me lie down in green pastures, he leads me beside quiet waters. – Psalm 23:2",
        "In peace I will lie down and sleep, for you alone, Lord, make me dwell in safety. – Psalm 4:8",
        "The Lord bless you and keep you; the Lord make his face shine on you and be gracious to you. – Numbers 6:24-25",
        "If it is possible, as far as it depends on you, live at peace with everyone. – Romans 12:18",
        "The God of peace will soon crush Satan under your feet. – Romans 16:20",
        "Mercy, peace and love be yours in abundance. – Jude 1:2"
    ],
    "hope": [
        "For I know the plans I have for you, declares the Lord, plans for welfare and not for evil, to give you a future and a hope. – Jeremiah 29:11",
        "The Lord is my light and my salvation; whom shall I fear? The Lord is the stronghold of my life; of whom shall I be afraid? – Psalm 27:1",
        "But those who hope in the Lord will renew their strength. – Isaiah 40:31",
        "We have this hope as an anchor for the soul, firm and secure. – Hebrews 6:19",
        "Be strong and take heart, all you who hope in the Lord. – Psalm 31:24",
        "May the God of hope fill you with all joy and peace as you trust in him. – Romans 15:13",
        "There is surely a future hope for you, and your hope will not be cut off. – Proverbs 23:18",
        "The eyes of the Lord are on the righteous, and his ears are attentive to their cry. – Psalm 34:15",
        "And hope does not put us to shame, because God’s love has been poured out into our hearts. – Romans 5:5",
        "The Lord delights in those who fear him, who put their hope in his unfailing love. – Psalm 147:11",
        "But as for me, I will always have hope; I will praise you more and more. – Psalm 71:14",
        "Why, my soul, are you downcast? Put your hope in God, for I will yet praise him. – Psalm 42:11",
        "Let us hold unswervingly to the hope we profess, for he who promised is faithful. – Hebrews 10:23",
        "To them God has chosen to make known among the Gentiles the glorious riches of this mystery, which is Christ in you, the hope of glory. – Colossians 1:27",
        "Through him we have also obtained access by faith into this grace in which we stand, and we rejoice in hope of the glory of God. – Romans 5:2"
    ],
    "strength": [
        "I can do all things through Christ who strengthens me. – Philippians 4:13",
        "The Lord is my strength and my shield; my heart trusts in him, and he helps me. – Psalm 28:7",
        "The Lord will fight for you; you need only to be still. – Exodus 14:14",
        "It is God who arms me with strength and keeps my way secure. – 2 Samuel 22:33",
        "Finally, be strong in the Lord and in his mighty power. – Ephesians 6:10",
        "My flesh and my heart may fail, but God is the strength of my heart and my portion forever. – Psalm 73:26",
        "The Lord is my strength and my song; he has become my salvation. – Exodus 15:2",
        "God is our refuge and strength, an ever-present help in trouble. – Psalm 46:1",
        "He gives strength to the weary and increases the power of the weak. – Isaiah 40:29",
        "The Lord gives strength to his people; the Lord blesses his people with peace. – Psalm 29:11",
        "Be on your guard; stand firm in the faith; be courageous; be strong. – 1 Corinthians 16:13",
        "The Sovereign Lord is my strength; he makes my feet like the feet of a deer. – Habakkuk 3:19",
        "I love you, Lord, my strength. – Psalm 18:1",
        "The Lord is the everlasting God, the Creator of the ends of the earth. He will not grow tired or weary. – Isaiah 40:28",
        "Wait for the Lord; be strong and take heart and wait for the Lord. – Psalm 27:14"
    ],
    "lust": [  # Quotes about resisting temptation, lust, or sexual immorality
        "But I say to you that everyone who looks at a woman with lustful intent has already committed adultery with her in his heart. – Matthew 5:28",
        "Flee from sexual immorality. Every other sin a person commits is outside the body, but the sexually immoral person sins against his own body. – 1 Corinthians 6:18",
        "No temptation has overtaken you that is not common to man. God is faithful, and he will not let you be tempted beyond your ability. – 1 Corinthians 10:13",
        "Put to death, therefore, whatever belongs to your earthly nature: sexual immorality, impurity, lust, evil desires and greed. – Colossians 3:5",
        "For everything in the world—the lust of the flesh, the lust of the eyes, and the pride of life—comes not from the Father but from the world. – 1 John 2:16",
        "But each person is tempted when they are dragged away by their own evil desire and enticed. – James 1:14",
        "Let marriage be held in honor among all, and let the marriage bed be undefiled, for God will judge the sexually immoral and adulterous. – Hebrews 13:4",
        "So I say, walk by the Spirit, and you will not gratify the desires of the flesh. – Galatians 5:16",
        "How can a young man keep his way pure? By guarding it according to your word. – Psalm 119:9",
        "Do not let sin reign in your mortal body so that you obey its evil desires. – Romans 6:12",
        "Watch and pray so that you will not fall into temptation. The spirit is willing, but the flesh is weak. – Matthew 26:41",
        "Create in me a clean heart, O God, and renew a right spirit within me. – Psalm 51:10",
        "Turn my eyes from looking at worthless things; and give me life in your ways. – Psalm 119:37",
        "For this is the will of God, your sanctification: that you abstain from sexual immorality. – 1 Thessalonians 4:3",
        "Blessed is the man who remains steadfast under trial, for when he has stood the test he will receive the crown of life. – James 1:12"
    ]
}

get_quote = input("Do you want a Bible quote based on your mood? (y/n): ")

if get_quote.lower() == "y":
    mood = input("Enter your mood (sad, happy, peace, hope, strength, lust): ").lower()
    if mood in bible_quotes:
        print(random.choice(bible_quotes[mood]))
    else:
        print("Sorry, I don't have quotes for that mood. Please try again.")
else:
    print("May God bless you!")