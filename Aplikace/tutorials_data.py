# basic tutorials
basic_tutorials = {
            "Jak otevřít soubor s daty": [
                (
                    "V nabídce 'Soubor' zvolte 'Otevřít soubor...'.\n"
                    "Tento krok vám umožní vyhledat a otevřít existující Excelové nebo CSV soubory ve vašem počítači.",
                    "no_image"
                ),
                (
                    "Vyberte soubor, který chcete otevřít, a potvrďte jeho výběr.",
                    "no_image"
                ),
                (
                    "Soubor se otevře a zobrazí se na nové záložce.\n"
                    "Nyní si můžete zobrazit a analyzovat data v uživatelsky přívětivém rozhraní.",
                    "no_image"
                ),
                (
                    "Ujistěte se, že data ve vašem souboru jsou ve správném formátu:\n"
                    "- První řádek musí obsahovat názvy sloupců.\n"
                    "- Pod ním musí být řádky s daty.\n"
                    "Pokud není tento formát dodržen, aplikace nemusí správně fungovat.",
                    "no_image"
                )
            ],
            "Jak zobrazit základní statistiky": [
                (
                    "Vyberte záložku s daty, které chcete analyzovat.\n"
                    "Tento krok zajistí, že pracujete s datovou sadou, na které chcete provést statistickou analýzu.",
                    "no_image"
                ),
                (
                    "Klikněte na tlačítko 'Zobrazit statistiky' v rámci záložky.\n"
                    "Po kliknutí se zobrazí okno se základními statistickými údaji.",
                    "no_image"
                ),
                (
                    "Prohlédněte si statistické údaje prezentované v novém okně.\n"
                    "Tyto statistiky zahrnují průměry, mediány, rozptyly a další užitečné metriky, které vám pomohou rychle pochopit hlavní charakteristiky vašich dat.",
                    "resources/basic_helper_pictures/statistics.png"
                )
            ],
            "Jak generovat grafy": [
                (
                    "Vyberte záložku s daty, pro která chcete vytvořit graf.\n"
                    "Zajistíte tak, že graf bude obsahovat správná data.",
                    "no_image"
                ),
                (
                    "Klikněte na 'Zobrazit graf' a vyberte požadovaný typ grafu.\n"
                    "Můžete zvolit z různých typů grafů jako jsou sloupcové, spojnicové, bodové, histogramy a další.",
                    "no_image"
                ),
                (
                    "Nastavte parametry grafu a poté graf vygenerujte.\n"
                    "Graf si můžete přizpůsobit podle potřeb vaší analýzy a následně jej uložit nebo exportovat.",
                    "no_image"
                ),
                (
                    "Pokud potřebujete, můžete si zobrazit nápovědu ke grafům přímo v aplikaci.\n"
                    "Tím se ujistíte, že vyberete správný typ grafu pro vaše data.",
                    "no_image"
                )
            ],
            "Lineární regrese": [
                (
                    "Vyberte datovou sadu, pro kterou chcete provést lineární regresi.\n"
                    "Regrese umožňuje nalézt vztahy mezi dvěma proměnnými.",
                    "no_image"
                ),
                (
                    "Vyberte proměnné pro osy X a Y, které chcete analyzovat.\n"
                    "Proměnné by měly být spojité, aby byla regrese smysluplná.",
                    "no_image"
                ),
                (
                    "Proveďte lineární regresi a zobrazte výsledky.\n"
                    "Výsledky zahrnují regresní přímku a koeficienty, které popisují vztah mezi proměnnými.",
                    "resources/basic_helper_pictures/regression_example.png"
                )
            ],
            "Analýza korelací": [
                (
                    "Vyberte tabulku pro analýzu korelací.\n"
                    "Tento krok zajistí, že máte data, která chcete porovnat.",
                    "no_image"
                ),
                (
                    "Spusťte analýzu korelací pro zjištění vztahů mezi sloupci.\n"
                    "Korelaci lze použít k identifikaci silných a slabých vztahů mezi proměnnými.",
                    "no_image"
                ),
                (
                    "Prohlédněte si matici korelacní a zjistěte, které proměnné jsou pozitivně nebo negativně korelované.\n"
                    "Matice korelací vám poskytne přehled o tom, jak silně spolu jednotlivé proměnné souvisí.",
                    "resources/basic_helper_pictures/correlation_example.png"
                )
            ],
            "Spojení více datových tabulek": [
                (
                    "Vyberte více tabulek, které chcete spojit do jedné datové sady pomocí ctrl + levý klik.\n"
                    "Tímto krokem zajistíte, že budete pracovat s kompletními daty.",
                    "no_image"
                ),
                (
                    "Spojte tabulky a prohlédněte si výsledky spojení v nové záložce.\n"
                    "Spojení tabulek vám umožní kombinovat informace z různých zdrojů do jednoho souboru pro snadnější analýzu.",
                    "no_image"
                )
            ],
            "Agregace": [
                (
                    "Vyberte tabulku, ve které chcete provést agregaci.\n"
                    "Agregace vám umožní shrnout data a získat přehledné souhrny.",
                    "no_image"
                ),
                (
                    "Proveďte agregaci a zobrazte výsledky.\n"
                    "Toto je užitečné pro rychlé shrnutí dat a získání přehledu o průměrných hodnotách.",
                    "no_image"
                )
            ]
}

graph_tutorials = {
            "Spojnicový graf": [
                (
                    "Vyberte záložku s daty, která obsahují časové řady nebo jiné spojité údaje.\n"
                    "Spojnicové grafy jsou ideální pro zobrazení trendů v čase.",
                    "no_image"
                ),
                (
                    "Klikněte na 'Zobrazit graf' a vyberte 'Spojnicový graf'.\n"
                    "Nastavte osu X jako časovou osu (např. roky) a osu Y jako měřenou veličinu (např. počet studentů).",
                    "no_image"
                ),
                (
                    "Generujte graf a analyzujte zobrazené trendy.\n"
                    "Tento typ grafu vám umožní identifikovat období růstu nebo poklesu.",
                    "resources/graph_helper_pictures/line_graph_example.png"
                )
            ],
            "Sloupcový graf": [
                (
                    "Vyberte záložku s daty, která chcete porovnávat mezi různými kategoriemi.\n"
                    "Sloupcové grafy jsou skvělé pro porovnání množství mezi různými skupinami.",
                    "no_image"
                ),
                (
                    "Klikněte na 'Zobrazit graf' a vyberte 'Sloupcový graf'.\n"
                    "Nastavte osu X jako kategorie (např. města) a osu Y jako měřenou veličinu (např. počet studentů).",
                    "no_image"
                ),
                (
                    "Generujte graf a porovnejte hodnoty mezi různými kategoriemi.\n"
                    "Tento typ grafu je ideální pro vizualizaci rozdílů v datech.",
                    "resources/graph_helper_pictures/bar_graph_example.png"
                )
            ],
            "Bodový graf": [
                (
                    "Vyberte záložku s daty, která chcete analyzovat pro korelaci mezi dvěma proměnnými.\n"
                    "Bodové grafy jsou užitečné pro identifikaci vztahů mezi proměnnými.",
                    "no_image"
                ),
                (
                    "Klikněte na 'Zobrazit graf' a vyberte 'Bodový graf'.\n"
                    "Nastavte osu X a osu Y podle proměnných, které chcete porovnávat (např. věk a příjem).",
                    "no_image"
                ),
                (
                    "Generujte graf a analyzujte vzory a korelace mezi proměnnými.\n"
                    "Tento typ grafu pomáhá odhalit vztahy mezi datovými body.",
                    "resources/graph_helper_pictures/scatter_plot_example.png"
                )
            ],
            "Histogram": [
                (
                    "Vyberte záložku s daty, která chcete analyzovat pro frekvenční rozdělení.\n"
                    "Histogramy jsou užitečné pro zobrazení distribuce hodnot v datech.",
                    "no_image"
                ),
                (
                    "Klikněte na 'Zobrazit graf' a vyberte 'Histogram'.\n"
                    "Nastavte osu X jako hodnoty a osu Y jako frekvenci výskytu těchto hodnot.",
                    "no_image"
                ),
                (
                    "Generujte graf a analyzujte rozdělení hodnot v datech.\n"
                    "Histogramy vám pomohou identifikovat vzorce, jako je šikmost nebo bimodalita.",
                    "resources/graph_helper_pictures/histogram_example.png"
                )
            ],
            "Kruhový diagram": [
                (
                    "Vyberte záložku s daty, která chcete zobrazit jako části celku.\n"
                    "Kruhové diagramy jsou ideální pro zobrazení procentuálního rozložení kategorií.",
                    "no_image"
                ),
                (
                    "Klikněte na 'Zobrazit graf' a vyberte 'Kruhový diagram'.\n"
                    "Nastavte jednotlivé kategorie a jejich hodnoty, které chcete porovnat.",
                    "no_image"
                ),
                (
                    "Generujte graf a analyzujte podíl jednotlivých kategorií.\n"
                    "Tento typ grafu vám umožní vizuálně porovnat části celku.",
                    "resources/graph_helper_pictures/pie_chart_example.png"
                )
            ],
            "Krabicový graf": [
                (
                    "Vyberte záložku s daty, která chcete analyzovat pro rozložení hodnot.\n"
                    "Krabicové grafy jsou užitečné pro zobrazení mediánu, kvantilů a odlehlých hodnot.",
                    "no_image"
                ),
                (
                    "Klikněte na 'Zobrazit graf' a vyberte 'Krabicový graf'.\n"
                    "Nastavte data pro zobrazení rozložení hodnot v různých kategoriích.",
                    "no_image"
                ),
                (
                    "Generujte graf a analyzujte rozložení hodnot.\n"
                    "Krabicové grafy vám pomohou identifikovat rozsah a variabilitu dat.",
                    "resources/graph_helper_pictures/box_plot_example.png"
                )
            ],
            "Geografický graf": [
                (
                    "Vyberte záložku s daty, která obsahují informace o městech nebo geografických lokalitách.\n"
                    "Geografické grafy jsou užitečné pro zobrazení geografických dat na mapě.",
                    "no_image"
                ),
                (
                    "Klikněte na 'Zobrazit graf' a vyberte 'Geografický graf'.\n"
                    "Zvolte sloupec s názvy měst, které chcete zobrazit na mapě.",
                    "no_image"
                ),
                (
                    "Po volbě měst se aplikace na chvíli může zaseknout, protože převádí názvy měst na souřadnice.\n"
                    "Tento proces umožňuje aplikaci správně zobrazit data na mapě.",
                    "no_image"
                ),
                (
                    "Generujte graf a analyzujte geografickou distribuci dat.\n"
                    "Tento typ grafu vám pomůže vizuálně identifikovat koncentrace a rozložení dat na mapě.",
                    "resources/graph_helper_pictures/geographic_map_example.png"
                )
            ]
}




# advanced scenarios
advanced_scenarios = {
            "Trendy ve vývoji počtu studentů v čase": [
                (
                    "Formulace otázky: Jaký je trend ve vývoji počtu studentů vysokých škol v České republice v průběhu času?\n\n"
                    "Úvod do problematiky: Pochopení trendů ve vývoji počtu studentů na vysokých školách je klíčové pro mnoho zainteresovaných stran. "
                    "Pro studenty je důležité vědět, jaké jsou jejich šance na přijetí a kolik dalších lidí mohou očekávat jako své spolužáky či budoucí konkurenty na trhu práce. "
                    "Pro vysoké školy tato statistika umožňuje plánovat kapacity a rozvoj infrastruktury, což je klíčové pro zajištění kvalitního vzdělávání. "
                    "Kromě toho mohou vlády a vzdělávací instituce využívat tyto údaje k vytváření politik a strategií, které podporují rozvoj vzdělávacího systému.",
                    "no_image"
                ),
                (
                    "Analýza dat: Pro analýzu dat byly použity soubory z Ministerstva školství, mládeže a tělovýchovy (MŠMT), konkrétně tabulky F1 Souhrny, "
                    "tabulky s celkovými počty studentů a odhady potenciálních studentů vycházející z tabulky o počtu obyvatel ze statistického úřadu. "
                    "Níže jsou uvedeny jednotlivé kroky analýzy. Data jsme nahráli do aplikace a následně začali analyzovat.",
                    "no_image"
                ),
                (
                    "Vývoj počtu studentů v letech 2001-2022: Na obrázku je zobrazen počet studentů vysokých škol v letech 2001 až 2022. "
                    "Tento graf ukazuje, že počet studentů rostl do roku 2010, kdy dosáhl vrcholu, a následně začal klesat. "
                    "Od roku 2018 můžeme pozorovat mírný nárůst, který pokračuje až do roku 2022.",
                    "resources/figures/1/celkem.png"
                ),
                (
                    "Demografické trendy: Pro analýzu demografických trendů jsme použili spojnicový graf, který zobrazuje počet narozených dětí v daných letech. "
                    "Tento graf poskytuje kontext pro predikci možného počtu potenciálních studentů. Na obrázku je patrný nárůst počtu narozených dětí v 70. letech, známý jako 'Husákovy děti'. "
                    "Tento baby boom byl výsledkem pronatalitní politiky prezidenta Gustáva Husáka, která vedla k výraznému zvýšení porodnosti.",
                    "resources/figures/1/narozeni.png"
                ),
                (
                    "Porovnání celkového počtu studentů s odhadem potenciálních nových studentů: Na obrázku je porovnán celkový počet studentů s odhadem potenciálních nových studentů, "
                    "založeným na demografických datech. Tento odhad počítá pouze s možným počtem nových studentů v daném roce a nezahrnuje již studující studenty, což může vést k podhodnocení celkového počtu.",
                    "resources/figures/1/celkem_potencial.png"
                ),
                (
                    "Porovnání potenciálních nových studentů s počtem nově zapsaných studentů: Na obrázku je zobrazen počet potenciálních nových studentů ve srovnání s počtem studentů, "
                    "kteří se poprvé zapsali do vysoké školy. Je patrné, že počet nově zapsaných studentů se v průběhu let mění, což může být ovlivněno demografickými změnami a dalšími faktory.",
                    "resources/figures/1/poprve_zapsani.png"
                ),
                (
                    "Regresní analýza: Pro analýzu trendů v datech jsme použili lineární regresní analýzu, která porovnává dvě proměnné. "
                    "Na obrázku je zobrazen graf s lineární regresní čarou, která ukazuje celkový trend mezi rokem a celkovým počtem studentů.",
                    "resources/figures/1/regrese_stud.png"
                ),
                (
                    "Regresní analýza potenciálních nových studentů: Tento graf ukazuje vztah mezi počtem potenciálních studentů a celkovým počtem nově zapsaných studentů. "
                    "Tento výsledek může indikovat demografické změny a potenciální budoucí výzvy pro vysoké školy v oblasti náboru studentů.",
                    "resources/figures/1/regrese_potencial.png"
                ),
                (
                    "Interpretace výsledků: Při analýze dat jsme zjistili, že celkový počet studentů dosáhl vrcholu v roce 2010 a poté klesal, ale od roku 2018 začal opět růst. "
                    "Tento trend je viditelný jak v grafu celkového počtu studentů, tak v regresní analýze. Odhad potenciálního počtu nových studentů ukazuje, že počet nových uchazečů o studium klesá, "
                    "což může ovlivnit budoucí trendy v počtu studentů.",
                    "no_image"
                ),
                (
                    "Shrnutí a závěr: Na základě výše uvedené analýzy můžeme konstatovat, že dlouhodobý trend počtu studentů na vysokých školách je rostoucí, ačkoli v letech 2010-2018 došlo k poklesu. "
                    "Tento trend je důležitý pro studenty i školy z hlediska plánování a strategického rozhodování. Pro přesnější analýzu by bylo vhodné zahrnout i data o již studujících studentech. "
                    "Celkový růst počtu studentů naznačuje, že vysokoškolské vzdělání je stále důležitější a poptávka po něm roste. Hypotéza byla potvrzena, protože dlouhodobý trend ukazuje na růst počtu studentů, i přes období poklesu mezi lety 2010 a 2018.",
                    "no_image"
                ),
                (
                    "Otázky pro studenty:\n"
                    "1. Jaký byl trend v počtu studentů od roku 2001 do roku 2010? Co se změnilo po roce 2010?\n"
                    "2. Jak mohou demografické změny, jako například 'Husákovy děti', ovlivnit počet studentů na vysokých školách?\n"
                    "3. Proč je důležité porovnávat počet nově zapsaných studentů s potenciálním počtem nových studentů?\n"
                    "4. Co nám může regresní analýza říci o budoucích trendech v počtu studentů? Jaké faktory by mohly tento trend ovlivnit?",
                    "no_image"
                )
            ],


            "Vztah mezi národností studenta a typem studia": [
                (
                    "Formulace otázky: Zahraniční studenti častěji volí prezenční formu studia než čeští studenti.\n\n"
                    "Úvod do problematiky: Forma studia může výrazně ovlivnit studijní zkušenost a akademické výsledky studentů. "
                    "Zatímco čeští studenti mohou preferovat kombinované nebo distanční formy studia, které jim umožňují skloubit studium s prací nebo jinými povinnostmi, "
                    "zahraniční studenti často volí prezenční formu studia. To může být způsobeno několika faktory, jako je potřeba intenzivní jazykové a kulturní integrace, "
                    "vyšší náklady na život v cizí zemi nebo specifické požadavky stipendijních programů, které často vyžadují plnou účast na studiu.",
                    "no_image"
                ),
                (
                    "Zahraniční studenti se také často snaží maximalizovat svůj akademický a sociální zážitek během omezené doby pobytu v hostitelské zemi. "
                    "Prezenční forma studia jim umožňuje více se zapojit do univerzitního života, což může zahrnovat přístup k různým akademickým a sociálním aktivitám, "
                    "lepší možnosti networkingu a získání hlubšího porozumění místní kultuře a akademickému prostředí.",
                    "no_image"
                ),
                (
                    "Analýza dat: Pro analýzu dat byly použity soubory z Ministerstva školství, mládeže a tělovýchovy (MŠMT), konkrétně tabulky obsahující data o formách studia "
                    "(prezenční a kombinované) rozdělené podle národnosti studentů. Níže jsou uvedeny jednotlivé kroky analýzy.",
                    "no_image"
                ),
                (
                    "Data o formách studia českých a zahraničních studentů: Na obrázcích je zobrazen počet studentů ve formě prezenčního a kombinovaného studia rozdělený podle českých a zahraničních studentů. "
                    "Použili jsme spojnicové grafy pro vizualizaci rozdílů mezi těmito dvěma skupinami studentů.",
                    "no_image"
                ),
                (
                    "Počet českých studentů ve formě prezenčního a kombinovaného studia.",
                    "resources/figures/2/celkem_p_k_cesi.png"
                ),
                (
                    "Počet zahraničních studentů ve formě prezenčního a kombinovaného studia.",
                    "resources/figures/2/celkem_p_k_cizinci.png"
                ),
                (
                    "Analyzovali jsme grafy, abychom identifikovali trendy a rozdíly v preferencích formy studia mezi českými a zahraničními studenty.",
                    "no_image"
                ),
                (
                    "Data o formách studia podle stupně studia: Na obrázcích jsou zobrazeny detaily o počtu českých studentů v jednotlivých stupních studia (bakalářské, magisterské, navazující magisterské a doktorské) podle formy studia.",
                    "no_image"
                ),
                (
                    "Počet českých studentů ve formě prezenčního studia podle stupně studia.",
                    "resources/figures/2/celkem_p_mix_cesi.png"
                ),
                (
                    "Počet českých studentů ve formě kombinovaného studia podle stupně studia.",
                    "resources/figures/2/celkem_k_mix_cesi.png"
                ),
                (
                    "Počet zahraničních studentů ve formě prezenčního studia podle stupně studia.",
                    "resources/figures/2/celkem_p_mix_cizinci.png"
                ),
                (
                    "Počet zahraničních studentů ve formě kombinovaného studia podle stupně studia.",
                    "resources/figures/2/celkem_k_mix_cizinci.png"
                ),
                (
                    "Porovnání prezenčního a kombinovaného studia českých a zahraničních studentů: Na obrázku je zobrazen počet studentů ve formě prezenčního a kombinovaného studia pro české i zahraniční studenty dohromady.",
                    "no_image"
                ),
                (
                    "Počet studentů ve formě prezenčního a kombinovaného studia (čeští a zahraniční studenti dohromady).",
                    "resources/figures/2/celkem_p_k_cesi_cizinci_dohromady.png"
                ),
                (
                    "Tyto grafy slouží k vizualizaci počtu studentů v různých formách a stupních studia. Umožňují nám identifikovat a interpretovat rozdíly mezi českými a zahraničními studenty, "
                    "což je klíčové pro pochopení jejich preferencí a studijních návyků.",
                    "no_image"
                ),
                (
                    "Interpretace výsledků: Analýza dat ukazuje, že zahraniční studenti mají tendenci volit prezenční formu studia častěji než čeští studenti. "
                    "Důvody mohou být různé:\n\n"
                    "1. Jazyková a kulturní integrace: Zahraniční studenti často potřebují intenzivní jazykovou praxi a kulturní adaptaci, což jim prezenční studium umožňuje lépe než distanční formy.\n"
                    "2. Finanční a stipendijní podmínky: Mnoho zahraničních studentů studuje na základě stipendií, která často vyžadují plnou účast na studiu.\n"
                    "3. Maximalizace zážitku: Zahraniční studenti chtějí během svého omezeného pobytu v hostitelské zemi získat co nejvíce z akademického a sociálního života.\n"
                    "4. Akademické požadavky: Některé programy, zvláště na úrovni magisterských a doktorských studií, mohou vyžadovat intenzivní laboratorní a výzkumné práce, které jsou lépe realizovatelné v prezenční formě.",
                    "no_image"
                ),
                (
                    "Naopak čeští studenti, kteří mají možnost studium kombinovat s prací nebo jinými závazky, často volí kombinované nebo distanční formy studia.",
                    "no_image"
                ),
                (
                    "Shrnutí a závěr: Z analýzy dat vyplývá, že zahraniční studenti preferují prezenční formu studia ve srovnání s českými studenty. "
                    "Tato preference může být způsobena potřebou intenzivní integrace, finančními a stipendijními podmínkami a snahou maximálně využít pobyt v hostitelské zemi. "
                    "Tyto poznatky jsou důležité pro univerzity, které mohou na základě těchto informací lépe plánovat a přizpůsobovat své programy a služby jak pro české, tak pro zahraniční studenty.",
                    "no_image"
                ),
                (
                    "Otázky pro studenty:\n"
                    "1. Proč mohou zahraniční studenti preferovat prezenční formu studia více než čeští studenti?\n"
                    "2. Jaké faktory mohou ovlivnit rozhodnutí českých studentů preferovat kombinované nebo distanční formy studia?\n"
                    "3. Jaké jsou výhody a nevýhody prezenčního studia pro zahraniční studenty?\n"
                    "4. Jak mohou univerzity využít informace o preferencích forem studia pro plánování a přizpůsobení svých programů?",
                    "no_image"
                )
            ],

            "Geografické rozložení studentů": [
                (
                    "Formulace otázky: Která města mají nejvyšší počet studentů a jaký je jejich podíl na celkovém počtu studentů v letech 2001 a 2022?\n\n"
                    "Úvod do problematiky: Geografické rozložení studentů je klíčovým faktorem pro plánování a rozvoj vzdělávací infrastruktury. "
                    "Města s vysokou koncentrací studentů často čelí specifickým výzvám i příležitostem, které ovlivňují nejen vzdělávací instituce, ale i místní ekonomiku a sociální strukturu. "
                    "Faktory ovlivňující koncentraci studentů ve velkých městech zahrnují dostupnost a kvalitu vysokých škol, životní náklady, možnosti bydlení, pracovní příležitosti a kulturní a společenský život.",
                    "no_image"
                ),
                (
                    "Analýza dat: Data o počtu studentů podle měst byla načtena a zpracována pro roky 2001 a 2022. Grafy zobrazují počet studentů v jednotlivých městech a umožňují identifikovat města s nejvyšší koncentrací studentů v daných letech.",
                    "no_image"
                ),
                (
                    "Geografické rozložení studentů v roce 2001. Tento typ grafu, využívající mapy s kruhy různé velikosti, ukazuje koncentraci studentů v jednotlivých městech. "
                    "Větší kruhy indikují vyšší počet studentů, což usnadňuje rychlé vizuální porovnání mezi městy.",
                    "resources/figures/3/2001.png"
                ),
                (
                    "Počet studentů v jednotlivých městech v roce 2001. Tato tabulka uvádí přesný počet studentů pro každé město, což je užitečné pro detailnější analýzu a srovnání.",
                    "resources/figures/3/2001_pocty.png"
                ),
                (
                    "Počet studentů v prvních deseti městech v roce 2001. Tento graf zaměřuje na nejvýznamnější města, což umožňuje lepší pochopení rozdílů mezi nimi.",
                    "resources/figures/3/2001_prvnich10.png"
                ),
                (
                    "Geografické rozložení studentů v roce 2022. Opět jsou větší kruhy indikátorem vyššího počtu studentů.",
                    "resources/figures/3/2022.png"
                ),
                (
                    "Počet studentů v jednotlivých městech v roce 2022. Stejně jako v roce 2001, i v roce 2022 dominují Praha a Brno.",
                    "resources/figures/3/2022_pocty.png"
                ),
                (
                    "Počet studentů v prvních deseti městech v roce 2022. Podobně jako v roce 2001, Praha stále vede s výrazným náskokem před Brnem a dalšími městy.",
                    "resources/figures/3/2022_prvnich10.png"
                ),
                (
                    "Tyto grafy a tabulky jsou zásadní pro vizualizaci dat, protože umožňují rychlé porovnání a identifikaci hlavních trendů a rozdílů. "
                    "Geografické zobrazení koncentrace studentů v různých městech napomáhá při rozhodování o budoucích investicích a rozvoji vzdělávací infrastruktury.",
                    "no_image"
                ),
                (
                    "Interpretace výsledků: Na základě analýzy dat bylo zjištěno, že Praha a Brno mají nejvyšší koncentraci studentů v obou sledovaných letech. "
                    "Tento trend je pravděpodobně způsoben kvalitou a počtem vysokých škol v těchto městech, které přitahují studenty z celé republiky i ze zahraničí. "
                    "Města jako Olomouc a Plzeň také vykazují významný počet studentů, což naznačuje, že jsou důležitými vzdělávacími centry.",
                    "no_image"
                ),
                (
                    "Identifikace měst s nejvyšší koncentrací studentů a možných důvodů:\n\n"
                    "1. Praha: Hlavní město s nejvyšší koncentrací prestižních vysokých škol, jako je Univerzita Karlova, České vysoké učení technické, Vysoká škola ekonomická, Česká zemědělská univerzita a další. "
                    "Praha také nabízí široké možnosti kulturního a společenského vyžití, což přitahuje studenty.\n"
                    "2. Brno: Druhé největší město v České republice, domov pro Masarykovu univerzitu, Vysoké učení technické v Brně a další významné instituce. "
                    "Brno je také známé svou inovativní a technologickou scénou.\n"
                    "3. Olomouc: Univerzita Palackého v Olomouci je jednou z nejstarších univerzit v České republice a přitahuje studenty svou dlouhou historií a akademickou kvalitou.\n"
                    "4. Plzeň: Západočeská univerzita v Plzni je významnou institucí v regionu a nabízí širokou škálu studijních programů.",
                    "no_image"
                ),
                (
                    "Další faktory, které mohou ovlivňovat koncentraci studentů, zahrnují dostupnost bydlení, možnosti pracovních příležitostí během studia a po jeho ukončení, a také celkovou kvalitu života v daném městě.",
                    "no_image"
                ),
                (
                    "Shrnutí a závěr: Na základě výše uvedené analýzy lze konstatovat, že Praha a Brno dominují v počtu studentů jak v roce 2001, tak v roce 2022. Olomouc a Plzeň také patří mezi města s vysokou koncentrací studentů. "
                    "Tento trend je pravděpodobně způsoben kombinací kvalitních vzdělávacích institucí, bohaté kulturní nabídky a dobrých životních podmínek v těchto městech.\n\n"
                    "Potvrzuje se tedy hypotéza, že nejvyšší počet studentů je soustředěn ve velkých městech, která nabízejí nejlepší podmínky pro studium a život. "
                    "Tato informace je klíčová pro plánování rozvoje vysokého školství a infrastruktury v České republice.",
                    "no_image"
                ),
                (
                    "Otázky pro studenty:\n"
                    "1. Která města mají nejvyšší počet studentů v letech 2001 a 2022?\n"
                    "2. Jaké faktory mohou přispívat k vysoké koncentraci studentů v Praze a Brně?\n"
                    "3. Proč je důležité zkoumat geografické rozložení studentů pro plánování vzdělávací infrastruktury?\n"
                    "4. Jaké další faktory kromě kvality vzdělávacích institucí mohou ovlivňovat rozhodnutí studentů o studiu v určitém městě?",
                    "no_image"
                )
            ],

            "Geografické rozložení zahraničních studentů v České republice": [
                (
                    "Formulace otázky: Jaké jsou změny v geografickém rozložení zahraničních studentů mezi lety 2001 a 2022?\n\n"
                    "Úvod do problematiky: Geografické rozložení zahraničních studentů je klíčovým faktorem pro pochopení dynamiky a atraktivity různých měst a regionů v rámci České republiky. "
                    "Významné změny v počtu zahraničních studentů mohou signalizovat růst atraktivity určitých měst díky kvalitě vzdělání, životním podmínkám nebo ekonomickým a kulturním faktorům.",
                    "no_image"
                ),
                (
                    "Analýza dat: Pro analýzu byly použity údaje o počtu zahraničních studentů v jednotlivých městech v letech 2001 a 2022. "
                    "Data zahrnují mapové vizualizace a tabulky top 10 měst s nejvyšším počtem zahraničních studentů.",
                    "no_image"
                ),
                (
                    "Data pro rok 2001 jsou uvedena v tabulce a mapě. Největší počet zahraničních studentů se v roce 2001 soustředil v Praze (4677), následován Brnem (1672) a Olomoucí (669).",
                    "no_image"
                ),
                (
                    "Top 10 měst s nejvyšším počtem zahraničních studentů v roce 2001.",
                    "resources/figures/4/top10_2001.png"
                ),
                (
                    "Geografické rozložení zahraničních studentů v roce 2001.",
                    "resources/figures/4/2001_mapa.png"
                ),
                (
                    "Data pro rok 2022 jsou uvedena v tabulce a mapě. V roce 2022 je nárůst počtu zahraničních studentů patrný v Praze (27767), Brně (14829) a Olomouci (2650).",
                    "no_image"
                ),
                (
                    "Top 10 měst s nejvyšším počtem zahraničních studentů v roce 2022.",
                    "resources/figures/4/top10_2022.png"
                ),
                (
                    "Geografické rozložení zahraničních studentů v roce 2022.",
                    "resources/figures/4/2022_mapa.png"
                ),
                (
                    "Vývoj počtu zahraničních studentů v letech 2001 až 2022. Data ukazují stabilní nárůst počtu zahraničních studentů během těchto let, což naznačuje rostoucí atraktivitu českých vysokých škol pro studenty ze zahraničí.",
                    "resources/figures/4/pocet_cizincu_ve_vsech_letech.png"
                ),
                (
                    "Interpretace výsledků: Z výše uvedených grafů a tabulek je zřejmé, že počet zahraničních studentů na českých vysokých školách se od roku 2001 do roku 2022 výrazně zvýšil. "
                    "V roce 2001 bylo v České republice pouze několik tisíc zahraničních studentů, zatímco v roce 2022 tento počet přesáhl 54 000. Nejvýraznější nárůst byl zaznamenán v Praze a Brně, "
                    "kde se počet zahraničních studentů výrazně zvýšil. V roce 2022 bylo v Praze více než 27 000 zahraničních studentů, což je více než pětinásobek počtu z roku 2001.",
                    "no_image"
                ),
                (
                    "Dalším důležitým městem je Brno, kde se počet zahraničních studentů rovněž významně zvýšil. V roce 2001 bylo v Brně 1672 zahraničních studentů, zatímco v roce 2022 tento počet vzrostl na 14829. "
                    "Další města, jako jsou Olomouc, Plzeň, Ostrava a Hradec Králové, také zaznamenala nárůst počtu zahraničních studentů, i když ne v takové míře jako Praha a Brno.",
                    "no_image"
                ),
                (
                    "Důvody pro studium v Česku: Podle zprávy DZS (Dům zahraniční spolupráce) z roku 2023 jsou hlavními důvody pro volbu studia v České republice vidět na obrázku.",
                    "no_image"
                ),
                (
                    "Důvody pro studium v Česku (Zdroj: DZS - Zpráva o zahraničních studentech na českých vysokých školách 2023, 2023).",
                    "resources/figures/4/graf_duvody.png"
                ),
                (
                    "Dle výzkumu zahraničních studentů provedeného Domem zahraniční spolupráce (DZS) je kvalita vzdělání nejdůležitějším kritériem při volbě Česka jako destinace ke studiu. "
                    "Kvalitu nabízených oborů si kladou za cíl zhodnotit a do určité míry zaručit mezinárodní univerzitní žebříčky.",
                    "no_image"
                ),
                (
                    "Shrnutí a závěr: Na základě výše uvedené analýzy lze konstatovat, že počet zahraničních studentů na českých vysokých školách významně vzrostl od roku 2001 do roku 2022. "
                    "Přestože Praha a Brno přitahují největší počet zahraničních studentů, i ostatní města zaznamenávají nárůst. "
                    "Kvalita vzdělání, konkrétní studijní program a kulturní nebo jazyková blízkost jsou hlavními důvody pro volbu Česka jako studijní destinace.",
                    "no_image"
                ),
                (
                    "Otázky pro studenty:\n"
                    "1. Jaké města přitahovala nejvíce zahraničních studentů v letech 2001 a 2022?\n"
                    "2. Co může být důvodem pro výrazný nárůst počtu zahraničních studentů v Praze a Brně?\n"
                    "3. Jak mohou různé faktory, jako je kvalita vzdělání nebo kulturní blízkost, ovlivnit rozhodnutí zahraničních studentů studovat v České republice?\n"
                    "4. Jaké změny v geografickém rozložení zahraničních studentů jste zaznamenali mezi lety 2001 a 2022 a co by mohlo tyto změny způsobit?",
                    "no_image"
                )
            ],


            "Rozdíl mezi soukromými a veřejnými školami": [
                (
                    "Formulace otázky: Jaký je rozdíl v počtu studentů a úspěšnosti mezi veřejnými a soukromými vysokými školami?\n\n"
                    "Úvod do problematiky: Vysoké školy v České republice lze rozdělit na veřejné a soukromé instituce. Rozdíly mezi nimi mohou ovlivnit nejen počet studentů, ale také jejich úspěšnost v dokončení studia. "
                    "Veřejné školy mají často delší tradici, širší nabídku oborů a jsou finančně podporovány státem. Na druhé straně soukromé školy mohou nabízet inovativní programy, flexibilní studijní podmínky a individuálnější přístup ke studentům. "
                    "Faktory jako finanční náklady, prestiž, kvalita vzdělání a možnosti kariérního uplatnění mohou ovlivnit volbu mezi soukromou a veřejnou vysokou školou.",
                    "no_image"
                ),
                (
                    "Analýza dat: Pro analýzu byly použity údaje z tabulky F12, která obsahuje data o počtu studentů na veřejných a soukromých vysokých školách v letech 2020 až 2022. "
                    "Předchozí roky nebyly rozděleny na veřejné a soukromé školy, a proto se zaměřujeme na data z těchto let. Byly vytvořeny srovnávací grafy pro porovnání počtu studentů a absolventů na těchto institucích.",
                    "no_image"
                ),
                (
                    "Data pro veřejné školy jsou uvedena v tabulce a grafu. Z grafů a tabulek je zřejmé, že počet studentů na veřejných vysokých školách je výrazně vyšší než na soukromých školách. "
                    "Počet studujících českých studentů se pohybuje kolem 230 000, zatímco počet poprvé zapsaných studentů je kolem 45 000 ročně. Počet absolventů se pohybuje kolem 46 000 ročně.",
                    "no_image"
                ),
                (
                    "Data o počtu studentů na veřejných vysokých školách.",
                    "resources/figures/5/verejne_tab.png"
                ),
                (
                    "Počet studentů na veřejných vysokých školách.",
                    "resources/figures/5/verejne_graf.png"
                ),
                (
                    "Data pro soukromé školy jsou uvedena v tabulce a grafu. Počet studentů na soukromých vysokých školách je výrazně nižší. "
                    "Počet studujících českých studentů se pohybuje kolem 22 000, počet poprvé zapsaných studentů je kolem 4 000 ročně, a počet absolventů je kolem 5 000 ročně.",
                    "no_image"
                ),
                (
                    "Data o počtu studentů na soukromých vysokých školách.",
                    "resources/figures/5/soukrome_tab.png"
                ),
                (
                    "Počet studentů na soukromých vysokých školách.",
                    "resources/figures/5/soukrome_graf.png"
                ),
                (
                    "Celkové počty studentů na veřejných a soukromých školách jsou srovnány v grafu. Je zřejmé, že počet studentů na veřejných školách je výrazně vyšší než na soukromých školách.",
                    "no_image"
                ),
                (
                    "Srovnání počtu studentů na veřejných a soukromých školách.",
                    "resources/figures/5/soukr_verej_pocet_studentu.png"
                ),
                (
                    "Interpretace výsledků: Na základě analýzy dat je zřejmé, že veřejné vysoké školy mají výrazně vyšší počet studentů než soukromé školy. "
                    "Možné důvody pro vyšší počet studentů a úspěšnost na veřejných školách mohou zahrnovat:\n\n"
                    "1. Tradiční povahu a delší historii veřejných škol.\n"
                    "2. Širší nabídku studijních programů.\n"
                    "3. Nižší finanční náklady díky státní podpoře.\n"
                    "4. Vyšší prestiž některých veřejných škol.",
                    "no_image"
                ),
                (
                    "Naopak soukromé školy mohou být atraktivní pro studenty hledající specifické obory, individuální přístup a flexibilní studijní podmínky.",
                    "no_image"
                ),
                (
                    "Z grafů a tabulek také můžeme odvodit následující poměry:\n\n"
                    "Veřejné školy:\n"
                    "1. Poměr absolventů vůči studujícím (2020-2022): přibližně 20.5 % (46 000 / 230 000).\n"
                    "2. Poměr absolventů vůči nově zapsaným (2020-2022): přibližně 102 % (46 000 / 45 000).\n\n"
                    "Soukromé školy:\n"
                    "1. Poměr absolventů vůči studujícím (2020-2022): přibližně 22.7 % (5 000 / 22 000).\n"
                    "2. Poměr absolventů vůči nově zapsaným (2020-2022): přibližně 125 % (5 000 / 4 000).",
                    "no_image"
                ),
                (
                    "Shrnutí a závěr: Na základě výše uvedené analýzy lze konstatovat, že veřejné vysoké školy mají výrazně vyšší počet studentů než soukromé školy. "
                    "Nicméně, pro přesné vyhodnocení úspěšnosti absolventů nejsou k dispozici potřebná data. Informace o absolventech neobsahují údaje o typech studia (bakalářské, magisterské, doktorské), "
                    "opakování ročníků ani jiné podrobnosti. Navíc, do roku 2019 nebyla v tabulce F12 sbírána data o veřejných a soukromých školách zvlášť, ale pouze dohromady. "
                    "Data v tabulce F12 jsou dostupná k jednotlivým školám, ale pro shrnující informaci o všech veřejných a soukromých školách se data začala uvádět až od roku 2020. "
                    "Tato analýza tedy poskytuje zjednodušený pohled na rozdíly mezi veřejnými a soukromými školami.",
                    "no_image"
                ),
                (
                    "Pro plné potvrzení nebo vyvrácení této hypotézy by bylo zapotřebí přesnějších údajů, zejména o jednotlivých oborech a opakování ročníků. "
                    "Tabulka F12 bohužel neposkytuje všechny potřebné informace, takže by bylo nutné dohledat jiné zdroje dat pro detailnější analýzu.",
                    "no_image"
                ),
                (
                    "Například touto problematikou se zabývá aplikace dropout.pef.czu.cz. Tato aplikace vznikla v rámci projektu „Stanovení postupu výpočtu ukazatele propadovosti studentů českých vysokých škol\" "
                    "podpořeného Technologickou agenturou ČR v letech 2016-2017 na České zemědělské univerzitě v Praze. Provozovatelem aplikace je Česká zemědělská univerzita v Praze, "
                    "anonymní data obsažená v aplikaci jsou poskytována Ministerstvem školství, mládeže a tělovýchovy z databáze Sdružených informací matrik studentů.",
                    "no_image"
                ),
                (
                    "Dalším zdrojem je projekt Česko v datech. Jedná se o unikátní projekt na poli datové žurnalistiky, který na základě analýzy aktuálních dat odhaluje zajímavá a mnoha lidem dosud neznámá fakta o naší zemi. "
                    "S těmito výstupy následně seznamuje veřejnost a dává je k dispozici médiím. Ta naše analýzy využívají pro vlastní články, pořady a reportáže. "
                    "Naší ambicí je vyhledávat témata, která jsou přitažlivá nebo důležitá pro celou společnost. Chceme objevit souvislosti, které se v datech skrývají, "
                    "a potvrdit či vyvrátit tvrzení, která se v české společnosti tradují, ale bez práce s rozsáhlými daty jim chybí důkaz.",
                    "no_image"
                ),
                (
                    "Otázky pro studenty:\n"
                    "1. Jaké jsou hlavní rozdíly mezi veřejnými a soukromými vysokými školami v České republice?\n"
                    "2. Jaké faktory mohou přispívat k vyššímu počtu studentů na veřejných vysokých školách?\n"
                    "3. Proč mohou někteří studenti preferovat soukromé vysoké školy navzdory nižšímu počtu studentů?\n"
                    "4. Jaké další údaje by bylo užitečné získat pro podrobnější analýzu úspěšnosti studentů na veřejných a soukromých školách?",
                    "no_image"
                )
            ]
        }
