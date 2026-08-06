---
id: "nara--47323287--community-relations-documentation-1970-47323287"
title: "Community relations documentation 1970 - 47323287"
source: NARA-RG615
source_url: "https://www.archives.gov/research/topics/uaps"
agency: "USAF"
record_type: "archival-record"
incident_date: ""
incident_location: ""
pages: 95
naid: ""
provenance: "NARA RG 615; scanned pages vision-transcribed with gemini-3-flash-preview - not verbatim OCR, verify quotes against source"
---

# Community relations documentation 1970 - 47323287

## Page 1

COORDINATION AND RECORD COPY

| FILE CODE | WRITE LAST NAME AND SHOW DATE COORDINATED |
| :--- | :--- |
| *Handwritten: File*<br>*Handwritten: 5-INF-2*<br>*Handwritten: DB* | *Handwritten: 2101*<br>*Handwritten: FCK* |

December 4, 1970

Mr. Enrico Grimaldi
14 Kings Park Road
Commack, NY 11725

Dear Mr. Grimaldi,

Your UFO sighting report was forwarded to this headquarters by Major Adams, Commander of the Montauk Air Station.

The Air Force Project Blue Book was terminated December 17, 1969.

Official Air Force policy subsequent to that date leaves action to be taken upon sighting a UFO to the individual. Therefore, we can make no official recommendations nor initiate any investigations. However, if you feel that your safety is threatened, we recommend consulting your local police department.

Sincerely,

Signed

FRANCIS C. MORIARTY, Maj, USAF
Director of Information

EBc

CONTROL NUMBER

| NAME OF WRITER AND TYPIST'S INITIALS | TEL EXT | DATE | NAME OF REWRITER AND TYPIST'S INITIALS | TEL EXT | DATE |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Lt DesRoches/db | | 4 Dec 70 | Major Moriarty/db | | 4 Dec 70 |

ADC FORM NOV 66 132

## Page 2

*Handwritten: Enrico Grimaldi*
*Handwritten: 14 Kings Park Rd.*
*Handwritten: Commack, N.Y. 11725*

*Handwritten: To Whom It May Concern:*

*Handwritten: I would like to report a U.F.O. sighting which took place on Saturday, Nov. 21, 1970 at 9:50 P.M. (E.S.T.). I was located at Commack, Long Island in my backyard, when the sighting took place.*

*Handwritten: The objects looked like faint stars, they moved in a straight line from north to south. They were in two rows and moved in a uniform pattern which I have drawn below.*

*Image: A hand-drawn diagram showing eight dots arranged in two staggered parallel columns of four. An arrow from the text points toward the dots. To the right of the dots, an arrow indicates the path of movement, labeled "DIRECTION OF TRAVEL".*

*Handwritten: I viewed the objects for approximately 2 or 3 seconds before they disappeared. There altitude above the horizon was about 60° or 70° degrees. They appeared between the constellations Orion*

## Page 3

*Handwritten: and the Square of Pegasus. The sky was very clear and no clouds were in sight. They appeared to be traveling at a very high altitude and were moving quiet fast.*

*Handwritten: I would like to know if there were any other reports concerning this specific sighting. Thank you.*

*Handwritten: Yours Truly,*
*Handwritten: Enrico Grimaldi*

## Page 4

## FOR OFFICIAL USE ONLY

**DEPARTMENT OF THE AIR FORCE**
**773D RADAR SQUADRON (SAGE) (ADC)**
**MONTAUK AIR FORCE STATION, NEW YORK 11954**

*Image: Seal of the Department of Defense, United States of America*

2 December 1970

REPLY TO ATTN OF: CC

SUBJECT: UFO Report

TO: 21st Air Div (OI)

1. Reference telecon between TSgt Owens this station and your agency on 1 December 1970.

2. Attached herewith is a letter from Mr Enrico Grimaldi concerning a UFO sighting of 21 November 1970, forwarded for your action.

*Handwritten: James L. Adams*
JAMES L. ADAMS, Major, USAF
Commander

1 Atch a/s

*Image: Large faint watermark of the Department of Defense seal in the center of the page.*

## FOR OFFICIAL USE ONLY

## Page 5

nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp

## Page 6

```

In []:
```python
import os
import base64
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def transcribe_image(image_path):
    base64_image = encode_image(image_path)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an expert at transcribing historical documents. Transcribe the provided image to clean Markdown, following the specified conventions."
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Transcribe this scanned government document page to clean Markdown, completely and faithfully. Conventions: classification banners as headings (## UNCLASSIFIED etc.); tables as Markdown tables; rubber stamps quoted inline as *Stamp: \"...\"*; handwriting as *Handwritten: ...*; every photo/sketch/diagram as *Image: <factual description>*; black-bar redactions as [REDACTED]; keep margin notes as italic asides. Output only the page content, no commentary."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ],
        max_tokens=4096
    )

    return response.choices[0].message.content

# Path to your image
image_path = "input_file_0.png"
transcription = transcribe_image(image_path)
print(transcription)

```

Out []:}
```output
CC

2 December 1970

UFO Report

21st Air Div (OI)

1. Reference telecon between TSgt Owens this station and your agency on 1 December 1970.

2. Attached herewith is a letter from Mr Enrico Grimaldi concerning a UFO sighting of 21 November 1970, forwarded for your action.

*Handwritten: James L. Adams*
JAMES L. ADAMS, Major, USAF &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1 Atch a/s
Commander

## FOR OFFICIAL USE ONLY

## Page 7

# MEMO
FROM THE OFFICE OF THE
COMMANDER

*Image: Emblem of the 21st NORAD Region, North American Air Defense Command, featuring a shield with a sword, wings, and a globe.*

To: *Handwritten: FRANK.*

*Handwritten: A FEW CHANGES*
*Handwritten: HAVE CHECKED FROM*
*Handwritten: CLASSIFICATION*
*Handwritten: STANDPOINT.*

*Handwritten: [Signature]*
GEORGE V. WILLIAMS
Major General, USAF

## Page 8

*Handwritten: File Pls*

*Handwritten: D* (underlined)

## Page 9

*Handwritten: File S-INF-2*
*Handwritten: AD*

# JOSEPH ALBINO
WRITER - PHOTOGRAPHER
FEATURES • ILLUSTRATIONS • AUDIO - VISUALS

221 Hillbrook Road
Syracuse, New York 13219
468-2171 (315)

November 11, 1970

Major Frank Moriarty
Director of Information
21ST NORAD REGION/AIR DIVISION
SAGE Building
Syracuse, New York

Dear Frank:

Enclosed is the article on NORAD (21ST NORAD REGION/AIR DIVISION) as written for the <u>Industrial Bulletin</u>.

This is a readable draft provided to insure against possible errors in facts or their interpretations. Do overlook any typing, spelling or grammatical errors which may have crept in. These will be dealt with in the final manuscript. Feel free to indicate your additions and deletions on the ms. pages.

Please sign and date the approval sheet which assures the editor you've read the article and found it factually correct. This corrected draft will be kept on file in my office. I may contact you again for additional information and/or pictures should the editor request same.

Incidentally, your signature on the approval sheet is not considered an endorsement of the fact you like or dislike, favor or disfavor the way in which the article was written. All articles are written on assignment and in accordance with the instructions given by the editor.

I'd appreciate return of the ms. as soon as possible since we have an immediate deadline to meet.

Thanks again for all.

Sincerely yours,

*Handwritten: Joe*
Joseph Albino

Enc.

## Page 10

Joseph Albino
221 Hillbrook Road
Syracuse, New York 13219

NORAD CONTRIBUTES TO
DEFENSE PLUS ECONOMY

By Joseph Albino

Picture yourself holding a huge umbrella over the vastness of the United States and Canada; an umbrella that protects this great nation from attack by bomb-carrying planes and air-breathing missiles. This is the picture of NORAD: The North American Air Defense Command with headquarter facilities carved out of ~~a huge~~ mountain ~~in Cheyenne, Wyoming.~~ *Handwritten: near Colorado Springs, Colo.*

Here in the northeast, including the New England states (except for the northern half of Maine), part of Pennsylvania, and New York State, our skies overhead are protected by the 21ST NORAD REGION.

*Handwritten: X* Commanded by *Handwritten: Air Force* Major General George V. Williams, 21ST's headquarters offices are located in the massive SAGE building at Hancock Airport,

*Handwritten: X* in Syracuse, *Handwritten: and are staffed by U.S. Air Force, Army, Navy and Canadian military personnel.*

-- MORE --

## Page 11

Albino -- 2 *Aside: Handwritten: Aerospace Defense Command's (ADC)*

*Aside: Handwritten: X* General Williams is also commander of 31 units in the / 21ST Air Division,^ *Handwritten: ~~the Air Force's~~ U.S. Air Force's contribution to NORAD. w7* Wearing his air division hat, the General's mission is to command, administer, train, equip, and generally prepare for their performance air force units located in the northeastern part of the United States, some radar squadrons in Canada, air bases in Greenland, and a fighter squadron plus radar squadrons in Iceland.

In addition, this air division commander also has operational responsibility for some air national guard units to insure they are properly trained and that their maintenance procedures are in accordance with air force standards.

Wearing his division hat, General Williams provides the aforementioned units to other operational commanders for the purpose of providing defense. He provides the units within the northeast to himself because, wearing his second hat, he is NORAD REGION commander for the northeast.

Of note, the General also provides a fighter squadron and radar squadrons at the tip of northern Maine and also in Canada to the 22ND NORAD REGION located at North Bay, Ontario. This region has a command post similar to SAGE in Syracuse only with a Canadian in command.

*Aside: Handwritten: X* In their operational capacity, these units perform their air defense role under the Canadian leader. They report to him. And respond to him. In addition, the General also provides ~~two~~ *Handwritten: one* fighter squadron~~s~~ and ~~A~~ *Handwritten: Two* radar squadrons to a Navy commander who is charged with the operational mission (~~in~~ *Handwritten: FIGHTING* the battle, so to speak).

-- MORE --

## Page 12

Albino -- 3

General Williams, in terms of his division hat, tends to think of himself as "administrator, housekeeper, doctor, judge, and janitor." However, when a division unit goes into battle, it operates under its operational commander.

Should there ever be an enemy air attack in the northeast, it would be the mission of the 21ST NORAD REGION, under General Williams, to provide the air defense for this area. He would have at his disposal air force units plus several army and navy commands.

*Handwritten: X* For example, ground-to-air ~~Bomarc~~ *Handwritten: NIKE* missiles protect Boston and New York. Though these army units are under the command of an Army commander in peace time, during an actual battle General Williams would command the forces from SAGE in Syracuse.

The heart of the SAGE (semi-automatic ground environment) system is a computerized system into which are electronically tied all of the air defense units in the NORAD region. Compilation of data is fed into the computer from the multitude of radar squadrons, providing an air picture for the scopes at SAGE.

*Handwritten: X* According to Captin James Shirey, *Handwritten: an* Intercept Director, "Because our radar squadrons are located on the borders of our NORAD region, we can see well beyond our geographic region. In fact, we can survey many, many thousands of square miles of sky.

"Using the data presented on the scopes and in the computer, we can detect incoming targets, identify them, conduct intercepts, determine whether these are friendly or hostile, and take whatever tactical action is appropriate.

-- MORE --

## Page 13

Albino -- 4

"We have here a capability of seeing tracks when they first come into our region through our surveillance section. Coupled with this is the identification section which identified *Handwritten: 3* ~~our~~ aircraft as friendly, unknown, or hostile. These two sections put their data into the computer which feeds it to the weapons section, the third section.

"We also have a manual input system which is responsible for inserting into the computer other information as, for example, weather information and flight plans, received from New York, Boston, Montreal, and Toronto. This additional data is a help to the weapons section in conducting its intercepts and completing missions."

*Margin note: X*
Training is continuous in the 21ST NORAD REGION, as is the case with ~~other~~ *Handwritten: ALL* North American Air Defense Command *Handwritten: Regions UNITS* located throughout

*Margin note: X*
the United States and Canada. At SAGE in Syracuse the weapons section, on a daily basis, ~~flies~~ *Handwritten: Controls jet fighters on* intercept missions and sends fighter squadrons on daily training flights to help pilots become more proficient with their aircraft.

In the event SAGE is destroyed, two back-up computer centers, located at isolated points, can together pick-up the air battle. Should these also be put out of operation, the radar squadrons can send their data directly to the NORAD center computers located within Cheyenne Mountain.

Too, in the event data lines feeding information from the radar squadrons to the computer were either destroyed or damaged, there exists an elaborate arrangement which allows communications to flow through a countless number of different routes to get from point to point.

-- MORE --

## Page 14

Albino -- 5

Sophisticated switching centers are located in fairly isolated areas. And there are many of them. In fact, according to SAGE authorities, the communications system of the 21ST NORAD REGION is probably the most redundant and survivable part of the entire complex.

SAGE also maintains its own power plant, and a very large one indeed, twenty-four hours a day. Though a great deal of commercial power is used, wherever this is the case a back-up system exists. Thus, the SAGE power plant can operate on its own in the event commercial power resources either are destroyed or power production falls low.

*Handwritten: X*
A word about the individual squadrons. At each radar squadron is a large search radar which is capable of detecting aircraft at altitudes from quite low to very high. This radar rotates through a *Handwritten: underline* 360 degree cycle and searches the entire area of sky within its range.

Co-located with the search radar is a height-finder radar which is capable of determining exactly how high an object is after its detection by the search radar. Though the search radar defines an object longitudinally and latitudinally, in order to run an intercept, it is necessary for the height-finding radar to determine whether the aircraft is, say, at five or fifty-thousand feet.

Too, at each site is a series of radio transmitters through which ground-control operators either talk to the interceptor pilots or send coded electronic instructions to unmanned missiles which can be guided electronically from the ground to the target. These transmitters are also tied to the SAGE computer and the two subordinate computers. This allows the weapons controller to control both interceptors and missiles electronically anywhere within the 21ST NORAD REGION area.

-- MORE --

## Page 15

Albino -- 6

Explains Captin Shirey, "We can either control an interceptor or let the computer control it entirely. Through the SAGE computer we can send coded electronic information to the aircraft, telling it how to steer, what altitude to fly to, and what course to fly. We can also tell the computer whether we want the aircraft to attack from the rear, the side, or the front. This is all accomplished by a coded message to the computer receiver aboard the aircraft.

"The pilot in the interceptor aircraft then has a choice. On the one hand, he can fly the plane manually, following the displays our instructions generate on his radar scope: The computer generates a dot in the center of the scope. If the pilot keeps the dot in the center of the radar scope, it will steer him to the target.

"On the other hand, he can turn his plane to automatic control, take his hands and feet off the controls, and watch as the aircraft, guided by the computer, automatically takes him to the target. All he has to do is move the throttle to reach the speed the computer indicates and squeeze the trigger when told to by the computer."

*Handwritten: Large blue X in left margin* Active fighter squadrons, *Handwritten: in New York* are maintained primarily at Griffiss Air Force Base and Niagara (Air Force Base.) *Handwritten: I AP, and OTIS Air Force Base in Massachusetts* With radar squadrons located at Lockport, Watertown, Saratoga Springs, and Montauk *Handwritten: Au*, on the extreme tip of Long Island.

*Handwritten: Blue arrow in left margin* Consider, for example, the *Handwritten: 49* 48th Fighter Interceptor Squadron located at Griffis, *Handwritten: AFB* near Rome. This squadron comprises twenty F106 fighter planes, twenty-four pilots, and 470 support personnel devoted to keeping the planes flying.

-- MORE --

## Page 16

Albino -- 7

"All of the pilots of the 49th have flown combat missions over Vietnam and Laos," notes Captain "Goose" Gowell, 49th FIS Information Officer. "This is also true of the ~~seven~~ other active and *Handwritten: Air National* guard squadrons located within the 21ST NORAD REGION."

*Margin note: X*

Though the F106, flown by the 49th, is primarily an interceptor aircraft, it is also a superb plane for aerial combat against other fighters and compares favorably with other fighter planes flown, Too, because this plane can refuel in flight, it is capable of service anywhere in the world as both interceptor and aerial combat plane.

The 49th squadron is constantly at top training. In the event of enemy attack, its planes can be airborne immediately. Under peace time conditions, fifteen minutes is the maximum time in which planes become airborne during a practice alert. However, under battle conditions, all planes must be in the air, and can be, within five minutes.

The SAGE computer keeps track of all these interceptor planes plus other large aircraft (excluding the small private planes), especially those approaching the northeast from the eastern Atlantic. When the SAGE personnel decide to track an aircraft, they put a computer tag on it, and the computer generates information on the speed, heading, and altitude.

This is done for training and, not too infrequently, when a plane is of special interest. As, for example, when aflight either is hijacked or is carrying the president or some other very important person. Naturally, any plane which is considered a possible enemy aircraft is followed with tremendous care.

-- MORE --

## Page 17

Albino -- 8

Actually, SAGE tracks many so-called iron curtain country commercial aircraft that are on authorized flight plans. Not too infrequently, these commercial flights stray off their flight plan because of navigation errors. Should a plane be an unknown, it is labeled as such. If the plane is not a friendly by any of the available data, an interceptor is sent to check it just as soon as the aircraft comes under SAGE surveillance.

More specifically, when SAGE picks-up on its radar scopes an aircraft in the seaward area where identification must be made, it has only two minutes to identify him as either friendly or unknown. At the close of that two minutes, if the plane has not been identified as a friendly, SAGE scrambles a fighter.

A preplanned procedure is followed to determine the aircraft's purpose. It's the mission of the interceptor to look at the plane and identify its type, markings, and number. To date, all unknowns checked by the 21St interceptors have been commercial airlines and identifiable as such.

Throughout the 21ST NORAD REGION there is great emphasis on safety, including ground safety, flight safety, and missile safety. A Chief of Safety with a staff of six safety personnel, all of them well trained by the Air Force and in civilian universities, is head-quartered at SAGE.

These men consider their prime duty to be the eyes and ears of the commander. They spend sixty percent of their time visiting the units with the hope of spotting a potential hazard and eliminating it before an accident occurs.

-- MORE --

## Page 18

Albino -- 9

The Air Force's basic philosophy of safety is that all accidents are preventable and that the only acceptable rate of accidents is the zero rate. At this writing, ~~SAGE~~ *Handwritten: THE 21ST DIVISION* holds one of the highest safety records in the Aerospace Defense Command: 4.5 accidents per 100,000 flying hours. This is considered a ~~high~~ *Handwritten: low* rate for the type of military aircraft flown.

Each fighter squadron is assigned a flight surgeon who is well trained in aviation medicine. He keeps a close eye on the pilots to insure there is no problem that could cause a hazardous situation during a military mission. In the event a condition arises which could possibly incapacitate a pilot, he is grounded either temporarily or permanently.

Should there be a flight accident, a nine-man accident investigation board, including advisors to the board, is immediately sent to the accident scene. Ground accidents are also investigated by safety personnel who have been taught investigation procedures. All accidents, of whatever type, are reported not only to SAGE but also to the Aerospace Defense Command.

Of note, two major unions represent the employees working at Hancock Field. These include The Service Employee International Union, local 200 and The National Association of Government Employees, local R246.

In addition, Western Union employees are represented by the United Telegraph Workers, local 42, and AT&T employees by the Communication Workers of America. Both AT&T and Western Union work on a contract basis with the government, and their employees work full time at SAGE.

MORE

## Page 19

Albino -- 10

The base commander and the union representatives confer quarterly to discuss mutual problems and to resolve them. In addition, the civilian personnel officer meets with the union representatives monthly to review daily problems which have arisen since the previous month's meeting. Too, through an open door policy, union representatives report infractions as these occur and before they become problematic.

"The result of union representation has been to improve working conditions," maintains Rose M. Della Valle, of the Chief Employe Management Development Branch of the Central Civilian Personnel Office. "I find we are inclined to accept matters as they stand until someone brings problems not previously recognized to the fore."

Adds Lloyd Olschewski, Divisional President for Local 200 of The Service Employee International Union, "We've developed a pleasant relationship with management representatives and have been able to discuss difficult matters freely and informally. The greatest benefit of all, however, is the fact we can talk to management. This has been made possible by the recent Presidential Orders which give federal employees the right to organize."

Obviously, the 21ST NORAD REGION contributes not only to the air defense of the northeast but also to its economic betterment. Some five-hundred plus employees alone are employed at SAGE, at high paying, highly skilled positions. In addition, the 21ST spends millions of dollars annually purchasing many of its product needs from local retail firms.

-- MORE --

## Page 20

Albino -- 11

Too, as is the case throughout the Air Force, the 21ST serves as a virtual job training center.  Many a young man, having completed his military obligation, has entered industry as a skilled computer technician.

"In my opinion, the SAGE computer gave a tremendous boost to the computer industry," concludes General V. Williams.  "When built in the early 1950s, it was the most sophisticated computer ever designed and the largest computer ever built.  I've had IBM people tell me they made a quantum jump in computer technology because of the SAGE program.  As a result, this country has benefited in computer technology.  Maybe the development would have come along anyway.  But I believe, from my conversations with the computer people, that it was speeded up by a number of years.  And gave us a world wide lead in computers.  With the result, this country has been paid back for its investment in full."

-- THE END --

## Page 21

*Handwritten: file 5-INF-2 DB*

*Image: Logo of a bell inside a square frame.*

**Silver Burdett Company** *A Division of General Learning Corporation*

Morristown, New Jersey 07960, 201-538-0400

Oct. 2, 1970

Francis C. Moriarty, Major, USAF
Director of Information
Department of the Air Force
Headquarters 21st Air Division (ADC)
Hancock Field
Syracuse, N.Y. 13225

Dear Major Moriarty,

Thank you for the packet which arrived swiftly bearing the pictures and map of the Thule Air Base.

And as you might have guessed- I do have two questions- in other words help help.

1. One of our objectives in this book is to teach scale of miles and this is another great spot to do it- so could you give us the scale of miles or enough information that we could figure out a scale of miles. For those young people age 8 we must use simple fractions or small numbers as 1" is 2 miles, or 1" is 1/4 mile.

   If you could give us the distance or a close estimate of the distance from top to bottom of the sketch and from right to left- we could figure it out-- if you don't happen to have the exact scale.

2. Is the air strip and air port- that is the strip and hangers etc near this part of the base construction- near enough tha we could show it on the map. If so could you tell me where it is.

We would greatly appreciate this information.

I just have to take a moment for a personal aside- a color print was included in the packet of a radar screen and the sun rising or setting low in the sky- and the most fantastic cloud formations. Do you know ( if you happen to remember the picture) is the big black cloud formation one of those wind storms that someone has named a "phase"?i^t is a thrilling photo.

Again thank you for your cooperation.

Sincerely,

*Handwritten: Marian Chambers*

( Marian Chambers, Senior Editor
Social Studies, Dept.)

## Page 22

COORDINATION AND RECORD COPY

| FILE CODE | *Handwritten: 5-INF-2* |
| :--- | :--- |
| *Handwritten: DB* | WRITE LAST NAME AND SHOW DATE COORDINATED |
| | *Handwritten: 210I* |
| | *Handwritten: FCM* |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |

## Page 23

DEPARTMENT OF THE AIR FORCE
HEADQUARTERS UNITED STATES AIR FORCE
WASHINGTON, D.C. 20330

*Image: Seal of the Department of Defense, United States of America*

28 SEP 1970

REPLY TO ATTN OF: SAFOIIA

SUBJECT: Survey Request - N.Y. Regional Planning and Development Board

TO: 21st Air Division
Office of Information
Hancock Field, N.Y. 13225

1. Reference the attached questionnaire.

2. There is no objection to Air Force agencies responding to the attached questionnaire with unclassified information, time and manpower permitting.

FOR THE CHIEF OF STAFF

*Handwritten: Miller Carpenter*
*Handwritten: for* LEO I. BEINHORN *Handwritten: Col USAF*
Colonel, USAF
Chief, Internal Information Division
Office of Information

Copy to:
ADC (ADCOIX)

Underwrite Your Country's Might - Buy U.S. Savings Bonds

## Page 24

COORDINATION AND RECORD COPY

| FILE CODE | |
| :--- | :--- |
| *Handwritten: 5-INF-2* | WRITE LAST NAME AND SHOW DATE COORDINATED |
| *Handwritten: DB* | *Handwritten: 2101* |
| | *Handwritten: Tom* |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
|

## Page 25

**DEPARTMENT OF THE AIR FORCE**
**4624TH SUPPORT SQUADRON, SAGE (ADC)**
**HANCOCK FIELD**
**SYRACUSE, NEW YORK 13225**

*Image: Seal of the Department of Defense, United States of America*

REPLY TO
ATTN OF: 46240I

SUBJECT: Attached                                        8 Sep 70

TO: 210I

The attached questionnaire is forwarded to you as per instructions on the attached correspondence. Good luck.

*Handwritten: [Signature]*
JEFFREY A. ROBINSON, Capt, USAF
Information Officer

## Page 26

DEPARTMENT OF THE AIR FORCE
HEADQUARTERS 21ST AIR DIVISION (ADC)
HANCOCK FIELD
SYRACUSE, NEW YORK 13225

*Image: Seal of the United States Department of Defense*

REPLY TO ATTN OF: JA
27 August 1970

SUBJECT: Questionnaire Regarding Security Police Resources (Central New York Regional Planning and Development Board)

TO: 4624 IGS
Hancock Fld, NY 13225

1. Your attention is invited to Air Force Regulation 171-2 and, especially, paragraph 2f(1).

2. Accordingly, the letter and its attached questionnaire should be coordinated with the Office of Information for both the 4624th Support Squadron and the 21st Air Division. They, in turn, will be required to forward the documentation to the appropriate agency of Headquarters, USAF.

*Handwritten: William F Hebert*
WILLIAM F. HEBERT, Colonel, USAF
Staff Judge Advocate

1 Atch
Ltr 18 Aug 70, CNY Regional Planning & Development Bd.

1st Ind

4624IGS
28 August 1970

TO: 4624OI

Request your agency review attached letter and questionnaire as per AFR 171-2, and then submit to 21st Air Division Office of Information. They, in turn, will be required to forward the documentation to the appropriate agency of Headquarters USAF.

*Handwritten: Alexander A. Reneski Jr.*
ALEXANDER A. RENESKI, JR, 2d Lt, USAF
Chief, Security Police

2 Atchs
1. Ltr, Central NY Regional Planning & Development Bd, 18 Aug 70
2. Questionnaire

## Page 27

*Image: A logo consisting of six square panels with stylized icons representing planning and development (e.g., buildings, leaves, water, industry, people, and the letters RPDB).*

**CENTRAL NEW YORK REGIONAL PLANNING AND DEVELOPMENT BOARD**
321 East Water Street Syracuse, New York 13202 315-422-8276 Robert C. Morris, Executive Director

18 August 1970

Department of the Air Force
Hancock Field
Thompson Road
North Syracuse, New York 13212

Dear Sir:

Central New York's Regional Planning and Development Board's Technical Advisory Committee on Crime Control (CRIMETAC) is, as you may be aware, recognized by the State as the official agency for regional planning in crime prevention, law enforcement, and criminal justice in the Central New York Region.

RPDB CRIMETAC has hired Syracuse University Research Corporation (SURC) to produce an inventory identifying all the agencies and organizations involved in, or related to, crime control activities in the five counties of Cayuga, Cortland, Madison, Onondaga, and Oswego, and to identify their resources.

We are contacting you in the thought that your resources -- even though not directly part of the "criminal justice system" -- should be taken into consideration since they could have applicability in special or emergency situations.

Naturally, your replies to this questionnaire in no way commit you or your agency to anything. The information you provide will be kept confidential and will not be released in any manner to identify you without your express written permission.

It is essential that CRIMETAC have complete basic information on the total resources of the area in order to plan and take action to improve the effectiveness of the region's crime-control activities. The inventory, once completed, will be available to all concerned agencies to assist them. Its success, however, depends upon your cooperation with SURC, which we have asked to deal with you directly in their project.

Our aim is to discover the agencies and their resources. The questions cannot, of course, include all of the possible variations of available information. As a result, we ask that you do not feel restricted by our questionnaire. If you have further reports, form samples, organization and operations charts, etc., they would be most welcome. We are, however, particularly interested in numbers of personnel, and any special capabilities of your organization.

## Page 28

Page Two

Let us again emphasize three points -- this information is urgently needed by CRIMETAC for effective planning of crime-control activities; any information that you give us is confidential and, when fully assembled, the total report can be of great value to you.

If you have any questions or comments on the inventory form, or if you would like to discuss it, please call Fred B. Smith, Director, Community Services Center, SURC, at (1-315) 477-8644. Your prompt response, of possible within two weeks of receipt of this questionnaire, will be appreciated.

Sincerely,

*Handwritten: Michael O Sawyer*

Michael O. Sawyer
Chairman

MOS:pac

## Page 29

SURC LE-3
(Public Law
Enforcemen

TECHNICAL ADVISORY COMMITTEE ON CRIME
CENTRAL NEW YORK REGIONAL PLANNING
AND DEVELOPMENT BOARD

INVENTORY OF AGENCIES
CONCERNED WITH CRIMINAL JUSTICE
AND CRIMINAL ACTIVITIES

INSTRUCTIONS

Please answer each question as it applies to your agency.

If you have questions about any item, please call:
1-315-477-8644 for assistance.

Where possible, please include samples of forms and
records used, and enclose any reports you may have on
your activities.

THE INFORMATION ON THIS INVENTORY IS CONFIDENTIAL

## Page 30

- 1 -

Inventory to Public Law Enforcement, Investigative
and Protective Service Agencies


Section I - General

1. Name of Organization_________________________________________________________
   _____________________________________________________________________________

2. Address _____________________________________________________________________
   ____________________________________________________ Phone Number ___________

3. What is the area covered by your organization?

   A. Village of ________________________
   B. Township of _______________________
   C. County of _________________________
   D. City of ___________________________
   E. Other (please describe area covered if it does
      not exactly match one of the above _______________________________________
      __________________________________________________________________________
      __________________________________________________________________________

4. What organization, government, or group procides the operating funds
   for your agency?
   _____________________________________________________________________________

5. What was your budget last year (calendar 1969) (enclose printed budget,
   if available; if not, please answer below):

   Wages $ ________________
   Other $ ________________


Section II - Training

1. "Basic training course for police" (240 hours, prescribed by Section 484,
   Article 19F, Executive Law of 1966).

   a. how many officers have completed this training? ___________
   b. how many completed this training in 1969? _________________
   c. how many are presently enrolled in this training? _________

2. "Advanced In-Service Police Training Course" (offered by the Office of
   Local Government, Division of Police)

   a. how many officers have completed this training? ___________
   b. how many completed this training in 1969? _________________
   c. how many are presently enrolled in this training? _________

## Page 31

3. "Course in Police Supervision" (Offered by the Office of Local Government
   Division of Police) .
    a. how many officers have completed this training? \_\_\_\_\_\_
    b. how many completed this training in 1969? \_\_\_\_\_\_
    c. how many are presently enrolled in this training? \_\_\_\_\_\_

Section III - Personnel

1. Please give number of personnel in each class.

| | | Time Employed | |
| :--- | :---: | :---: | :---: |
| **Rank** | **Full Time** | **Part time** | **Temporary** |
| --- | --- | --- | --- |
| **A. Uniformed** | | | |
| 1. Chief/Major/Sheriff | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 2. Deputy Chief/Under Sheriff | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 3. Inspector | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 4. Captain | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 5. Lieutenant | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 6. Sergeant | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 7. Corporal | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 8. Patrolman/Trooper/Deputy | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 9. Jail Guards | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 10. Traffic/School Guards | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 11. Court Attendants, etc. | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 12. Matrons, etc. | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 13. Other uniformed (specify) | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 14. Total | \_\_\_\_\_\_ | \_\_\_\_\_\_ | \_\_\_\_\_\_ |

**B. Civilian**

1. Clerical \_\_\_\_\_\_
2. Technical (specify) \_\_\_\_\_\_
3. Other (specify) \_\_\_\_\_\_
4. Total \_\_\_\_\_\_

Note: If you have an organization chart of your agency, please attach it to this form.

2. Please give the numbers of personnel assigned to:
    A. Headquarters and Administration \_\_\_\_\_\_
    B. Patrol \_\_\_\_\_\_
    C. Investigation \_\_\_\_\_\_
    D. Vice Activities \_\_\_\_\_\_
    E. Juvenile \_\_\_\_\_\_
    F. Organized Crime \_\_\_\_\_\_
    G. Records \_\_\_\_\_\_
    H. General Criminal Investigation \_\_\_\_\_\_

## Page 32

- 3 -

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;K. Support Facilities &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__________
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L. Training &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__________
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M. Recruiting &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__________
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N. Emergency &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__________
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O. Other (please specify) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__________

3. Do you employ police women? __________
   If yes, how many? __________

4. Do you have female attendants or matrons in your detention facilities? __________

5. Do you have a medical doctor on call at all times? __________

6. Do you have a psychologist or psychiatrist available to your department? __________

## Page 33

\- 4 -

Section III - Equipment

1. Does your agency have a separate building, space, or facility?

   Yes \_\_\_\_\_\_    No \_\_\_\_\_\_

2. Does your Department have <u>adequate</u> space for: (please check)

| | Adequate | Inadequate | None |
| :--- | :---: | :---: | :---: |
| General Working Space | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ |
| Records | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ |
| Communication | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ |
| Interview Rooms | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ |
| Storage of Equipment | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ |
| Office and Clerical Space | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ |
| Training Facilities and Classrooms | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ |
| Photography Work | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ |
| Laboratory Work | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ |

## Page 34

- 5 -

3. Do you have detention facilities for:
   (Please give number of available spaces)

| | Adults (over 21) | Youth (16 to 21) | Juveniles (16 & under) |
| :--- | :---: | :---: | :---: |
| **A. Pre-arraignment (24 hours or less)** | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Male | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Female | | | |
| **B. Post-arraignment to pre-adjudication** | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Male | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Female | | | |
| **C. Post Adjudication** | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Male | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Female | | | |

4. Does your facility accept or provide facilities for prisoners from:

| | Yes | No |
| :--- | :---: | :---: |
| A. Federal Agencies | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| B. State Police | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| C. Other State Agencies | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| D. City Police | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| E. Town, Village Police | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| F. County Sheriffs | \_\_\_\_\_\_ | \_\_\_\_\_\_ |

5. If you have no detention facilities, please indicate where you refer:

| | Detention Center | Location |
| :--- | :--- | :--- |
| A. Adults, Male | | |
| B. (over 21) Female | | |
| C. Youth (16 to 21) | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Male | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Female | | |
| D. Juvenile (under 16) | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Male | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Female | | |

## Page 35

\- 6 -

11. Do you have any of the following equipment? If yes, how many?

| A. Vehicles | With Radios | Without Radios |
| :--- | :---: | :---: |
| 1. Marked Patrol or Squad Cars | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 2. Unmarked Patrol or Squad Cars | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 3. Emergency Cars | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 4. Emergency Trucks | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 5. 2- or 3-wheel cycles | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 6. Command vehicles not shown above | \_\_\_\_\_\_ | \_\_\_\_\_\_ |
| 7. Special vehicles (give type) | | |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\

## Page 36

\- 7 -

C. Other than personal side arms, does your department have:

| | Number | How Many |
| :--- | :--- | :--- |
| Rifles (manual or semi-automatic) | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ |
| Pistols | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ |
| Full automatic weapons | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ |
| Shotguns or riot guns | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ |
| Gas guns or cannisters | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ |
| Gas grenades | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ |
| Special weapons (please specify type) | \_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_ |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\

## Page 37



## Page 38

*Handwritten: file*

<p align="center">COORDINATION AND RECORD COPY</p>

| FILE CODE | WRITE LAST NAME AND SHOW DATE COORDINATED |
| :--- | :--- |
| *Handwritten: 5-INF-2*<br>*Handwritten: DB* | *Handwritten: 210I* |
| | *Handwritten: FCM* |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |

<p align="center">September 28, 1970</p>

Miss Marion Chambers
Silver-Burdett Company
James Street
Morristown, New Jersey 07960

Dear Miss Chambers,

Enclosed are several photographs taken at Thule Air Base, Greenland. I hope these will be of some value in your forthcoming publication. Per our telephone conversation, I have requested the Information Office at Thule Air Base, Greenland, to send you additional photos and background information on the base.

If I can be of any further assistance, please feel free to call.

Sincerely,

*Stamp: "Signed"*

FRANCIS C. MORIARTY, Major, USAF
Director of Information

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<div align="right">CONTROL NUMBER</div>

| NAME OF WRITER AND TYPIST'S INITIALS | TEL EXT | DATE | NAME OF REWRITER AND TYPIST'S INITIALS | TEL EXT | DATE |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | | |

ADC FORM NOV 66 132

## Page 39

*Handwritten: File 5-INF-2 DB*

DEPARTMENT OF THE AIR FORCE
HEADQUARTERS AEROSPACE DEFENSE COMMAND
ENT AIR FORCE BASE, COLORADO 80912

*Image: Department of Defense seal*

*Handwritten: 5*

8 SEP 1970

Mr Ernest W Chard
Editor
Press-Herald

Dear Mr Chard

Providing proper protection for the nation against a surprise air attack on the United States is the responsibility of the Aerospace Defense Command (ADC). Our ability to carry out this responsibility should be of concern to most Americans.

Throughout the United States, ADC units share in providing air defense for our nation. ADC's aircrews and aircraft have been on continuous alert for the past twenty years to counter the threat of an attack by Soviet intercontinental bombers. In your area, Bangor International Airport is the operating location of ADC's Detachment One, 60th Fighter-Interceptor Squadron, which flies the supersonic F-101.

Heart and pulse of the aerospace defenses of the continent are located at the joint U.S.-Canadian North American Air Defense Command (NORAD) Combat Operations Center inside Cheyenne Mountain, near Colorado Springs. A visit to Colorado Springs is an opportunity for you to gather some meaningful and interesting stories for your readers. While here, you will be given extensive briefings on the Aerospace Defense Command's role in national security.

Please suggest a date for your visit via the enclosed envelope so we can arrange the necessary details. You may also call Area Code 303, 635-8911, extension 7343.

Also enclosed is a brochure highlightin the activities of aerospace defense, which may help you with some ideas for story possibilities. If you indicate your editorial needs, we will be happy to prepare an article for you.

Sincerely

*Stamp: "Signed by"*

JESSE J. FORD, JR., Captain, USAF
Chief, Public Information Division
Directorate of Information

2 Atch
1. Envelope
2. Brochure

Cy to: *Handwritten: [red checkmark]* 21 Air Div (OI)
60 FISq (CC)

## Page 40

*Handwritten: File 5-INF-82 DB*

*Image: Department of Defense Seal*

DEPARTMENT OF THE AIR FORCE
HEADQUARTERS AEROSPACE DEFENSE COMMAND
ENT AIR FORCE BASE, COLORADO 80912

8 SEP 1970
*Handwritten: S*

Mr Richard K Warren
Editor and Publisher
Bangor News

Dear Mr Warren

Providing proper protection for the nation against a surprise air attack on the United States is the responsibility of the Aerospace Defense Command (ADC). Our ability to carry out this responsibility should be of concern to most Americans.

Throughout the United States, ADC units share in providing air defense for our nation. ADC's aircrews and aircraft have been on continuous alert for the past twenty years to counter the threat of an attack by Soviet intercontinental bombers. In your area, Bangor International Airport is the operating location of ADC's Detachment One, 60th Fighter-Interceptor Squadron, which flies the supersonic F-101.

Heart and pulse of the aerospace defenses of the continent are located at the joint U.S.-Canadian North American Air Defense Command (NORAD) Combat Operations Center inside Cheyenne Mountain, near Colorado Springs. A visit to Colorado Springs is an opportunity for you to gather some meaningful and interesting stories for your readers. While here, you will be given extensive briefings on the Aerospace Defense Command's role in national security.

Please suggest a date for your visit via the enclosed envelope so we can arrange the necessary details. You may also call Area Code 303, 635-8911, extension 7343.

Also enclosed is a brochure highlighting the activities of aerospace defense, which may help you with some ideas for story possibilities. If you indicate your editorial needs, we will be happy to prepare an article for you.

Sincerely

*Stamp: "Signed by"*

JESSE J. FORD, JR., Captain, USAF
Chief, Public Information Division
Directorate of Information

2 Atch
1. Envelope
2. Brochure

Cy to: *Handwritten: (red slash)* 21 Air Div (OI)
60 FISq (CC)

## Page 41

*Handwritten: File 5-INF-32 OB*

DEPARTMENT OF THE AIR FORCE
HEADQUARTERS AEROSPACE DEFENSE COMMAND
ENT AIR FORCE BASE, COLORADO 80912

*Image: Seal of the Department of Defense, United States of America*

8 SEP 1970

Mr Paul S Plumer, Editor
Kennebec Journal

*Handwritten: S*

Dear Mr Plumer

Providing proper protection for the nation against a surprise air attack on the United States is the responsibility of the Aerospace Defense Command (ADC). Our ability to carry out this responsibility should be of concern to most Americans.

Throughout the United States, ADC units share in providing air defense for our nation. ADC's aircrews and aircraft have been on continuous alert for the past twenty years to counter the threat of an attack by Soviet intercontinental bombers. In your area, Bangor International Airport is the operating location of ADC's Detachment One, 60th Fighter-Interceptor Squadron, which flies the supersonic F-101.

Heart and pulse of the aerospace defenses of the continent are located at the joint U.S.-Canadian North American Air Defense Command (NORAD) Combat Operations Center inside Cheyenne Mountain, near Colorado Springs. A visit to Colorado Springs is an opportunity for you to gather some meaningful and interesting stories for your readers. While here, you will be given extensive briefings on the Aerospace Defense Command's role in national security.

Please suggest a date for your visit via the enclosed envelope so we can arrange the necessary details. You may also call Area Code 303, 635-8911, extension 7343.

Also enclosed is a brochure highlighting the activities of aerospace defense, which may help you with some ideas for story possibilities. If you indicate your editorial needs, we will be happy to prepare an article for you.

Sincerely

*Stamp: "Signed by"*
JESSE J. FORD, JR., Captain, USAF
Chief, Public Information Division
Directorate of Information

2 Atch
1. Envelope
2. Brochure

*Handwritten: [checkmark]* Cy to: 21 Air Div (OI)
60 FISq (CC)

## Page 42

nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp

## Page 43

DEPARTMENT OF THE AIR FORCE
648TH RADAR SQUADRON (SAGE) (ADC)
BENTON AIR FORCE STATION
BENTON, PENNSYLVANIA 17814

*Image: Seal of the Department of Defense, United States of America*

REPLY TO ATTN OF: OI/TSgt. Campbell
14 July 70

SUBJECT: Request for Photograph

TO: 21st Air Division (OI)
Hancock Field, Ny.

A formal request has been recived by this office from a commercial photographer to photograph the site for use on post cards.  Attached are copies of the 2 requests made by the AD/ART/PHOTO Service, Williamsport, Pa represented by Mr. Ralph E. Menne.  Request application be made through command channels to the OI, Secretary of the Air Force, Washington, D.C.

*Handwritten: James R Heller*
JAMES R. HELLER, 2nd Lt., USAF
Information Officer

## Page 44

OI/TSgt. Campbell  
14 July 70

Request for Photograph

21st Air Division (OI)  
Hancock Field, Ny.

A formal request has been recived by this office from a commercial photographer to photograph the site for use on post cards. Attached are copies of the 2 requests made by the AD/ART/PHOTO Service, Williamsport, Pa re- resented by Mr. Ralph E. Menne. Request application be made through command channels to the OI, Secretary of the Air Force, Washington, D.C.

*Handwritten: James R. Heller*  
JAMES R. HELLER, 2nd Lt., USAF  
Information Officer

## Page 45

AD/ART/PHOTO Service
P.O. BOX 524, WILLIAMSPORT, PA. 17701

PHOTOGRAPHY • BROCHURES
DESIGN ART AND LAYOUT
LOCAL VIEW POSTCARDS

June 16, 1970

Commanding Officer
Benton Air Force Station
R. D. #2
Benton, Penna. 17814

Dear Sir:

AD/ART/PHOTO Service is a distributor of Local View Post Cards throughout Northeastern Pa. We would like to make a Local View Post Card of the Benton Station, showing as much of the exterior of the facility that is permissible. If such a card were possible, it would be placed on sale to the general public at most retail outlets in the area. It may be of interest to your own PX facilities for the purpose of resale.

I would like permission to enter the B.A.F.S. for the purpose of securing photographs that will be used for the making of a Local View Post Card described above.

Thank you for your attention to this matter, I look forward to your reply.

Sincerely yours,

*Handwritten: Ralph E. Menne*
Ralph E. Menne (Jr)

REM/ju

*Handwritten: S/ AF*

*Handwritten: Reply Sent 8 July 70*
*Handwritten: Sgt Campbell*

## Page 46

*Image: Logo for "AD ART PHOTO Service" with a stylized camera lens icon and the word "Service" in script.*
P.O. BOX 524, WILLIAMSPORT, PA. 17701
PHONE (717) 368-2132

PHOTOGRAPHY • BROCHURES
DESIGN ART AND LAYOUT
LOCAL VIEW POSTCARDS
AERIAL PHOTOGRAPHY

July 10, 1970

Department Of The Air Force
648th. Radar Squadron (SAGE) (ADC)
Benton Air Force Station
Benton, Penna. 17814

Att: MSS/TSgt. Campbell:

Refer: Letter dated 7/8/70 - subject, photograph of site.

Dear Sgt. Campbell:

It is my desire to continue the effort to make a local view postcard that is indicative of the Benton Air Force Base for the purpose of retail resales to tourist visitors to the area. The scene depicted will be of a nature that will conform to Air Force security regulations as directed by your security officer. Transparencies will be submitted to the proper authority for approval before being printed on a postcard.

Thank you for your kind attention to this request.

Sincerely yours,

*Handwritten: Ralph E. Menne*
Ralph E. Menne (70)

REM/ju

*Handwritten: [faint scribble]*

## Page 47

DEPARTMENT OF THE AIR FORCE
HEADQUARTERS AEROSPACE DEFENSE COMMAND
ENT AIR FORCE BASE, COLORADO 80912

OFFICE OF THE COMMANDER

*Handwritten: File 5-INF-2 DB*
*Stamp: "14 JUL 1970"*
*Image: Seal of the Department of Defense, United States of America*

Major General George V. Williams
Commander, 21 Air Division

Dear George

Planning is now underway for the Eighteenth National Security Forum to be held at the Air War College. Tentatively, this year's forum is set for the second week in May 1971. Seventy-two distinguished civilian leaders (American citizens) will be invited to participate with the students of the college. Last year's forum was an outstanding success according to the commander of the Air University. Comments received from the guests showed that the time they spent contributed substantially to their better understanding of our national security problems and the role of the armed forces in our society.

Major air commanders have been asked to nominate prominent men and women who are interested in problems of our society and our national security. Since the forum's value is dependent upon the calibre of the guests, the nominees should represent the broadest possible cross section, with responsible representatives from all professions such as education, law, industry and religion; and, it is hoped, with greater representation from the <u>news media, labor, minority groups and local, state and federal governments.</u> In addition this year, special emphasis is being placed on youth. Nominees are to be chosen to assure the maximum exchange of diverse ideas and experiences between the guests and the Air War College students. The guests are to contribute to, and benefit from, the forum.

I have been urged to give ADC's nominations careful personal attention, and I would request that you give your personal attention to two nominees from your command.

Since only twenty-five per cent of those nominated can be invited, nominees should not be informed that their names were submitted until after final selections have been made. You will be advised which of your nominees are being invited and at that time you may contact them and urge them to attend.

A prerequisite for guest attendance is authorization to receive classified information up to and including SECRET; therefore, data on the attached biographical forms are needed. If these forms could be completed and returned to us no later than 5 Aug 1970, we will be able to meet our submission date to the Chief of Staff, General Ryan.

Sincerely

*Handwritten: H. A. Hanes*
H. A. HANES, Major General, USAF
Vice Commander

1 Atch
Biographical Data Forms (2)

## Page 48

# STAFF SUMMARY

| ROUTE TO | ACTION | SIGNATURE (GRADE AND SURNAME) | DATE | ORIGINATOR (OFC SYMBOL) | TEL NUMBER | DATE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 21CC | Action | | | 21OI | 304 | 31 Jul 70 |
| | | | | **SIGNATURE OF ACTION OFFICER** | | |
| | | | | *Handwritten: E. G. Stack* | | |
| | | | | **TYPED NAME AND GRADE OF ACTION OFFICER** | **TYPIST'S INITIALS** | |
| | | | | EDWARD G. STACK, Capt. | db | |
| | | | | Deputy Director of Information | | |

**SUBJECT**
Eighteenth National Security Forum

**SUMMARY**
1. Attached please find biographical outline of Mr. Mulroy and Mr. McDonald. I feel these two nominees would make excellent participants for the Eighteenth National Security Forum, per General Hanes's letter.

2. Recommend: Signature.

*Handwritten: E G Stack*
EDWARD G. STACK, Capt., USAF
Deputy Director of Information

*Handwritten: Signed due to short susp. However it seem somewhat parochial to choose both from Syracuse area - with entire Division to pick from WJ.*

***
ADC FORM JAN 67 172
*Hq ADC Field Printing Plant Ent AFB, Colorado*

## Page 49

COORDINATION AND RECORD COPY

*Handwritten: DIB*
| FILE CODE | *Handwritten: 5-INF 2* |
| :--- | :--- |
| **WRITE LAST NAME AND SHOW DATE COORDINATED** | *Handwritten: 210I* |
| | *Handwritten: FCM* |
| | *Handwritten: 26 Jun 70* |

210I &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; 26 June 1970

Defense Advisory Committee on Women in the Services (DACOWITS)

46240I

1. Headquarters ADC has directed that Paragraph 4 of attached SAFOI letter be complied with.

2. Request you work with the 4624 WAF Squadron Section Commander to set up a base orientation tour, as outlined in the SAFOI correspondence, for: Mrs. Marcia Ellingson, Rochester, NY. (appointed to DACOWITS in 1970). Her biography is attachment 2.

FOR THE COMMANDER

*Stamp: "SIGNED"* (inverted)

FRANCIS C. MORIARTY, Major, USAF &emsp; &emsp; &emsp; &emsp; 2 Atch
Director of Information &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; 1. SAFOI ltr, Defense Advisory Committee on Women in the Services
&emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; 2. DACOWITS Biographical Info on Members Appointed in 1970

| NAME OF WRITER AND TYPIST'S INITIALS | TEL EXT | DATE | NAME OF REWRITER AND TYPIST'S INITIALS | TEL EXT | DATE |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | | |
| | | | | | |

ADC FORM NOV 66 132 &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; CONTROL NUMBER

## Page 50

DEPARTMENT OF THE AIR FORCE
HEADQUARTERS UNITED STATES AIR FORCE
WASHINGTON, D.C.

*Image: Department of the Air Force seal*

REPLY TO ATTN OF: SAFOI

SUBJECT: Defense Advisory Committee on Women in the Services (DACOWITS)

TO: AU *Handwritten: [checkmark]* ADC MAC SAC AFSC CINCPACAF
AAC ATC TAC AFLC AFRES HQ COMD USAF

(Director of Information)

1. Annually, the Secretary of Defense appoints approximately 20 women to three-year terms as members of the Defense Advisory Committee on Women in the Services (DACOWITS). The new members will be selected on the basis of their reputations in a business, a profession, or public service and their record of civic leadership. We have been advised that this year the Committee will be losing Medical, Public Information and Professional Education representatives. Therefore, qualified nominees from these fields would be most appropriate and their chances for appointment to the Committee would be increased. A fact sheet on DACOWITS is inclosed (Atch 1).

2. The Air Force has been requested to submit nominations for the 1971 DACOWITS. Since geographic representation is also a selection criterion, only those commands with facilities in specified states will submit nominations to SAFOIC by 2 July 1970. These commands are: AAC, AU, ADC, AFLC, AFSC, ATC, CINCPACAF, HQ COMD USAF, MAC, TAC and SAC. Specific instructions for these commands concerning the submission of nominations are included as Attachment 2.

3. Recently, the Director of Women in the Air Force requested our assistance in orienting DACOWITS members to the Air Force and encouraging contact with individual DACOWITS members. A successful orientation program for the DACOWITS depends largely upon the support of information officers at all levels. Command information officers should establish and maintain close coordination with their command WAF Staff Directors in arranging activities for Committee members.

*Handwritten: [bracket next to paragraph 4]*
4. You are strongly encouraged to pay particular attention to the orientation of DACOWITS members by reviewing the current DACOWITS membership roster (Atch 4) and assuring

Underwrite Your Country's Might - Buy U.S. Savings Bonds

*Handwritten: Atch 1*

## Page 51

that the base listed beneath the name of each Committee membe
offers her a tour and briefing at that base by 31 December.
This orientation, whenever possible, should include visits to
those base activities where WAF and nurse personnel are
assigned. Additionally, DACOWITS members should be invited
to base-community functions and command orientation tours
frequently throughout the year.

5. For your information and use, biographical sketches of
Committee members are inclosed (Atch 5).

FOR THE CHIEF OF STAFF

*Handwritten: HL Hogan III*
H. L. HOGAN, III
Major General, USAF
Director of Information

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5 Atch
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Fact Sheet
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Nomination Instructions
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Biog Form
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. Membership Roster
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5. Biogs

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Copy to: OAR, AFAFC, AFCS,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;USAFA, USAFSS, SAF
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SAFOIL

2

## Page 52

Revised - May 19

<p align="center">DEFENSE ADVISORY COMMITTEE ON WOMEN IN THE SERVICES</p>

<p align="center">BIOGRAPHICAL INFORMATION<br>
ON MEMBERS APPOINTED IN 1970</p>

*Image: A large 'X' is drawn across the following section.*

<u>Mrs. William J. Bell (Lee Phillip), 209 East Lake Shore Drive, Chicago, Illinois 60611</u>

Native of Chicago, Illinois. Graduated Northwestern University (B.S.)
Business and Professional Affiliations: Director, Chicago Maternity Center; Past President and Director, Chicago Unlimited; Director, Academy of Television Arts and Sciences; Director, United Cerebral Palsy; Director, Chicago Heart Association; Director, Newberry Avenue Settlement House; Member, American Women in Radio and Television; - and Fashion Group of America.
Mrs. Bell, known professionally as Lee Phillip, is a television personality on CBS-WBBM-TV in Chicago, Illinois.

*Image: A large 'X' is drawn across the following section.*

<u>Mrs. Vivien H. Davenport, 1500 Mims Street, S.W., Atlanta, Georgia 30314</u>

Native of Washington, Georgia. Graduated Morris Brown College (B.S.); Atlanta University (M.S.L.S. and M.A. equivalent).
Member: Board of Directors, Association for the Blind; Alpha Kappa Alpha Sorority; National Education Association; Georgia Teachers and Education Association; Atlanta Teachers Association; Atlanta Library Association.
Business and Professional Affiliations: Atlanta Public Schools; Visiting Professor, Library Science Department, Albany State College, 1962; Georgia Special State Reading Program, 1964; Adult Education Affiliate; Director, ABE Night School Program.
Mrs. Davenport is a Librarian for the Atlanta Public Schools.

*Image: A large 'X' is drawn across the following section.*

<u>Mrs. Marcia Ellingson, 3940 East Avenue, Rochester, New York 14618</u>

Native of Newton, Massachusetts. Graduated Ohio State University (B.S.).
Member: Board member, Hochstein Memorial Music School; Health Assocation of Rochester & Monroe County, Tuberculosis Prevention Committee, 1943-53; Division Chairman, 1936 and Board Member, 1939-43, Rochester Civic Music Association; Board Member, League

*Handwritten: Catch 2*

## Page 53

<u>Mrs. Marica Ellingson (cont'd)</u>

of Women Voters (Board Member 1937-42); Chairman & Radio Publicity, American Red Cross, Blood Donor Service, 1941-42; Monroe County League for Planned Parenthood; Rochester Museum Association, Women's Council; American Association of University Women; Century Club; Founder and Past Board Member, Genesee Figure Skating Club; Board of Directors; Ars Antiqua; Honorary Chairman, Rochester Report on Job Horizons for Women Workshop of the Women's Council of the State of New York, Department of Commerce, 1962; President and Founder, "Woman Power".
Business and Professional Affiliations: Founder and Honorary President (1960) Rochester Institute of Technology Women's Club; Founder and Honorary Member (1965), Rochester Institute of Technology Women's Council; Member, sub-committee on Housing and Student Services Committee-New Campus Planning, 1965-66.
Awards: Civic Achievement Award - Rochester Federated Women's Clubs, 1963; 1967 Civic Award, Susan B. Anthony Republican Club; Governor Rockefeller's Roster of Outstanding Women, 1968.
Mrs. Ellingson is a Civic Leader.

*Image: A large 'X' is drawn across this section of text.*

<u>Mrs. Ellen K. Frautschi, 3206 Lake Mendota Drive, Madison, Wisconsin 53705</u>

Native of Madison, Wisconsin. Graduated University of Wisconsin (B.S.).
Member: Board Member, Madison Art Association; Madison Civic Music Association; Madison General Hospital Auxiliary (Board Member 1962).
Mrs. Frautschi is a Research Assistant, University Hospitals - Department of Pediatrics, Madison, Wisconsin.

*Image: A large 'X' is drawn across this section of text.*

<u>Mrs. Marilyn S. Fusfield, 42 Riverview Heights, Sioux Falls, South Dakota 57105</u>

Native of Sioux Falls, South Dakota. Graduated Bowling Green State University of Ohio (B.S.).
Member: Vice President, Family Service Board; Leader, Girl Scouts-Children's Home, 1949-56; Counselor and Member, Girl Scout-Board, 1956-62; Painter and Promoter, Civic Fine Arts; President, P.T.A. Garfield Elementary School, 1965; President, Sioux Falls Pan Hellenic, 1958; Delta Gamma National Social Fraternity; YWCA; Rotary Ann.

*Image: A large 'X' is drawn across this section of text.*

2

## Page 54

*Handwritten: 5-INF*
*Handwritten: DB*

DEPARTMENT OF THE AIR FORCE
HEADQUARTERS AEROSPACE DEFENSE COMMAND
ENT AIR FORCE BASE, COLORADO 80912

*Handwritten: 10 JUN 1970*

*Image: Seal of the Department of Defense*

REPLY TO ATTN OF: ADCIO-C

SUBJECT: Defense Advisory Committee on Women in the Services (DACOWITS)

TO:
| | | |
| :--- | :--- | :--- |
| 20 Air Div | 23 Air Div | 25 Air Div |
| *Handwritten: [checkmark]* 21 Air Div | 24 Air Div | 26 Air Div |

(Director of Information)

1. Your attention is invited to attached Hq USAF, SAFOI, correspondence regarding the selection of 1971 nominations for members of the Defense Advisory Committee on Women in the Services (DACOWITS).

2. Request you provide at least one, but no more than three nominations for the 1971 DACOWITS. Instructions for nominations are contained in Attachment 2 of the SAFOI correspondence. A copy of each nomination, in format prescribed in Attachment 3, will be forwarded to this headquarters (ADCIO-C) to arrive <u>not later than 24 June.</u> Special emphasis should be made to nominate qualified women from areas adjacent to ADC bases having WAF personnel assigned. All nominations should be coordinated with local WAF commanders.

3. Request you also work with local WAF commanders to set up base orientation tours as outlined in paragraph 4, SAFOI letter. Attachments 4, Membership Rosters, and 5, Biographical Information, afford useful information in this connection.

FOR THE COMMANDER

*Handwritten: [Signature]*
ARTHUR F. McCONNELL, JR, Lt Col, USAF
Deputy Director
Directorate of Information

1 Atch
Hq USAF Ltr, SAFOI, Undated,
w/5 Atchs

*Handwritten: [Signature]*
*Handwritten: Please handle.*
*Handwritten: No requirement for 21ST AD, Called into ADCIO-C, 18 June 70*

## Page 55

DEPARTMENT OF THE AIR FORCE
HEADQUARTERS UNITED STATES AIR FORCE
WASHINGTON, D.C.

*Image: Seal of the Department of Defense*

REPLY TO ATTN OF: SAFOI

SUBJECT: Defense Advisory Committee on Women in the Services (DACOWITS)

TO: AU *Handwritten: checkmark* ADC MAC SAC AFSC CINCPACAF
AAC ATC TAC AFLC AFRES HQ COMD USAF

(Director of Information)

1. Annually, the Secretary of Defense appoints approximately 20 women to three-year terms as members of the Defense Advisory Committee on Women in the Services (DACOWITS). The new members will be selected on the basis of their reputations in a business, a profession, or public service and their record of civic leadership. We have been advised that this year the Committee will be losing Medical, Public Information and Professional Education representatives. Therefore, qualified nominees from these fields would be most appropriate and their chances for appointment to the Committee would be increased. A fact sheet on DACOWITS is inclosed (Atch 1).

2. The Air Force has been requested to submit nominations for the 1971 DACOWITS. Since geographic representation is also a selection criterion, only those commands with facilities in specified states will submit nominations to SAFOIC by 2 July 1970. These commands are: AAC, AU, ADC, AFLC, AFSC, ATC, CINCPACAF, HQ COMD USAF, MAC, TAC and SAC. Specific instructions for these commands concerning the submission of nominations are included as Attachment 2.

3. Recently, the Director of Women in the Air Force requested our assistance in orienting DACOWITS members to the Air Force and encouraging contact with individual DACOWITS members. A successful orientation program for the DACOWITS depends largely upon the support of information officers at all levels. Command information officers should establish and maintain close coordination with their command WAF Staff Directors in arranging activities for Committee members.

*Handwritten: bracket to the left of paragraph 4*
4. You are strongly encouraged to pay particular attention to the orientation of DACOWITS members by reviewing the current DACOWITS membership roster (Atch 4) and assuring

Underwrite Your Country's Might - Buy U.S. Savings Bonds

## Page 56

that the base listed beneath the name of each Committee member offers her a tour and briefing at that base by 31 December. This orientation, whenever possible, should include visits to those base activities where WAF and nurse personnel are assigned. Additionally, DACOWITS members should be invited to base-community functions and command orientation tours frequently throughout the year.

5. For your information and use, biographical sketches of Committee members are inclosed (Atch 5).

FOR THE CHIEF OF STAFF

*Handwritten: HL Hogan III*
H. L. HOGAN, III
Major General, USAF
Director of Information

5 Atch
1. Fact Sheet
2. Nomination Instructions
3. Biog Form
4. Membership Roster
5. Biogs

Copy to: OAR, AFAFC, AFCS,
USAFA, USAFSS, SAFOIN,
SAFOIL

2

## Page 57

FACT SHEET

DEFENSE ADVISORY COMMITTEE
ON
WOMEN IN THE SERVICES

The Defense Advisory Committee on Women in the Services (better known by its short title DACOWITS) was established in 1951 by the Secretary of Defense. Limited to a membership of 50, DACOWITS is composed of civilian women who are selected as members on the basis of their outstanding reputations in business, a profession, or public service and their records of civic leadership. Equitable field-of-interest and geographical representation are also selection factors.

Members are appointed to DACOWITS by the Secretary of Defense for three years. They serve as individuals, not as official representatives of any group or organization with which they are affiliated. Semi-annual meetings are held in Washington, D. C.

The purposes of this civilian committee include: (1) to interpret to the public the need for and the role of women in the services and to promote public acceptance of military service as a career field for women, (2) to advise the Department of Defense on policies relating to women in the services, (3) to recommend measures to insure effective utilization of the capabilities of the women in the services, (4) to recommend standards for the training, housing, health, recreation and general welfare of women in the services.

Each DACOWITS member, in her particular field of interest and geographical area, endeavors to increase public acceptance of the concept of military service for women as a facet of good citizenship. To this end, the Committee develops and carries out a continuing and unified education program about women in the services -- Army WAC, Navy WAVES, Air Force WAF, Women Marines, Army Nurses, Navy Nurses, Air Force Nurses, Army Medical Specialists, Air Force Medical Specialists and Women's Specialists Section, Navy Medical Service Corps. They seek to promote understanding of the principal need for women in the armed forces in peacetime -- to maintain a nucleus of trained women to serve as the framework for absorbing thousands of women, utilizing their capabilities effectively and quickly, in case of national mobilization.

September 1968

## Page 58

# **INSTRUCTIONS FOR 1970 DACOWITS NOMINATIONS**

FOR:  AAC, AU, ADC, AFLC, AFSC, ATC, CINCPACAF, HQ COMD USAF,
      MAC, TAC, SAC

1.  Request you provide at least one, but not more than three nominations for the 1971 DACOWITS. Nominees must reside in one of the following states: Alabama, Alaska, Arizona, Arkansas, California, Hawaii, Idaho, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maryland, Michigan, Mississippi, Montana, Nevada, New Hampshire, New Mexico, North Carolina, North Dakota, Oregon, ~~Vermont~~, Virginia and Washington. In those states where more than one command has installations, cross command coordination will be effected to eliminate the possibility of duplicate nominations. In those states (Iowa, Kentucky and Vermont) which do not have extensive Air Force facilities, nominating responsibility is delegated as follows: Iowa and Vermont - SAC, Kentucky - MAC.

2.  The following information must be provided on each nominee: maiden name, place and date of birth, present home and business address, present employer, and husband's name, date and place of birth. Other details such as organizational affiliations, awards and honors, prior military service and as much additional information on each nominee as can be provided will assist greatly in making final selections. Three copies of all nominations will be submitted in the format shown in Atch 3. Since only a small percentage of those nominated can be appointed, discretion should be used in obtaining biographical information in order not to alert prospective nominees that they are under consideration for Committee membership. Assistance is selecting nominees will be obtained from command WAF Staff Directors.

3.  Nominations will be sent to HQ USAF (SAFOIC) to arrive not later than 2 July 1970.

Atch 2

## Page 59

Recommendation
for Nomination - DACOWITS
Revised May 1968

OFFICE OF THE ASSISTANT SECRETARY OF DEFENSE
(Manpower and Reserve Affairs)

DEFENSE ADVISORY COMMITTEE ON WOMEN IN THE SERVICES
DACOWITS SECRETARIAT - Room 3C972, The Pentagon
Washington, D.C. 20301

Date \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\

## Page 60

SCHOOLS OR COLLEGES ATTENDED:

| Name | Dates | Degrees |
| :--- | :--- | :--- |
| | | |
| | | |
| | | |
| | | |
| | | |

MILITARY SERVICE: (If Any)

| Dates | Branch | Rank |
| :--- | :--- | :--- |
| | | |
| | | |

SPOUSE'S FULL NAME: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\

## Page 61

The following information would be helpful in selection and should be listed, if known. The CANDIDATE BEING NOMINATED SHOULD NOT BE APPRISED THAT SHE IS BEING CONSIDERED FOR APPOINTMENT TO THE COMMITTEE.

BACKGROUND: Business or professional affiliations during the past 10 or more years. Any offices held.

________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________

MEMBERSHIP IN CLUBS OR ORGANIZATIONS:

| Club or Organization | Dates | Office Held |
| :--- | :--- | :--- |
| &nbsp; | &nbsp; | &nbsp; |
| &nbsp; | &nbsp; | &nbsp; |
| &nbsp; | &nbsp; | &nbsp; |
| &nbsp; | &nbsp; | &nbsp; |
| &nbsp; | &nbsp; | &nbsp; |
| &nbsp; | &nbsp; | &nbsp; |
| &nbsp; | &nbsp; | &nbsp; |
| &nbsp; | &nbsp; | &nbsp; |
| &nbsp; | &nbsp; | &nbsp; |
| &nbsp; | &nbsp; | &nbsp; |

## Page 62

```

In []:
```python
import os
import base64
from IPython.display import Image, display

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "test_images/page_11.png"

# Getting the base64 string
base64_image = encode_image(image_path)

```

In []:
```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Transcribe this scanned government document page to clean Markdown, completely and faithfully. Conventions: classification banners as headings (## UNCLASSIFIED etc.); tables as Markdown tables; rubber stamps quoted inline as *Stamp: \"...\"*; handwriting as *Handwritten: ...*; every photo/sketch/diagram as *Image: <factual description>*; black-bar redactions as [REDACTED]; keep margin notes as italic asides. Output only the page content, no commentary."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    max_tokens=1000
)

print(response.choices[0].message.content)

```

Out []:s
SORORITIES/SOCIETIES, HONORS/AWARDS, PUBLICATIONS:

________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## Page 63

*Revised - April 1970*

MEMBERSHIP ROSTER
DEFENSE ADVISORY COMMITTEE ON WOMEN IN THE SERVICES

Appointed in 1968

| | |
| :--- | :--- |
| Mrs. M. Bernard Aidinoff (Celia)<br>110 East End Avenue<br>New York, N. Y. 10028<br>(Member, Institute of International Education and Editor of Publications)<br>McGuire AFB | Miss Elaine Burnham<br>255 S. W. Harrison St., Apt 2F<br>Portland, Oregon 97201<br>(Facilities Supervisor, Pacific Northwest Bell Telephone Co.)<br>McChord AFB |
| Mrs. Charles Atkinson (Marian C.)<br>2560 North Summit Avenue<br>Milwaukee, Wisconsin 53211<br>(Guidance Department, Public School Board and Teacher, Social Improvement Program, Milwaukee Public Schools)<br>Gen Billy Mitchell Field | Mrs. Carroll C. Cannon (Helen H.)<br>108 South Izard Street<br>Forrest City, Arkansas 72335<br>(Co-owner St. Francis County Title & Abstract Co.)<br>Little Rock AFB |
| Mrs. Jeraldine J. Bostwick (Jeri)<br>2259 Kalakaua Avenue<br>Honolulu, Hawaii 96815<br>(Director, Public Relations and Advertising, Sheraton Hawaii Corp.)<br>Hickam AFB | Dr. Helen E. Clarke<br>3429 Duke Street<br>College Park, Maryland 20740<br>(Assoc. Dean of Students, Univ. of Md.)<br>Bolling AFB |
| Mrs. William W. Boyd, Jr. (Betty)<br>746 North Xenophon<br>Tulsa, Oklahoma 74127<br>(Broadcaster, Woman's Editor and Director of Public Service KTUL-TV)<br>Tinker AFB | Dr. Marjorie S. Dunlap<br>Dean, School of Nursing<br>University of California Medical Center<br>3rd and Parnassus Avenues<br>San Francisco, California 94122<br>Travis AFB |
| Mrs. C. Wayland Brooks (Mary)<br>1110 Watergate, West<br>Washington, D. C. 20037<br>(Superintendent, U. S. Mint)<br>Andrews AFB | Miss Beatrice Finkelstein<br>1517 Nichols Street<br>Manhattan, Kansas 66502<br>(Professor, College of Home Economics, Kansas State University)<br>Forbes AFB |
| Mrs. Janell Seitz Burke<br>Dean of Women<br>Idaho State University<br>Pocatello, Idaho 83201<br>Mountain Home AFB | Mrs. Thomas B. Fitzgerald (Sarah M.)<br>122 North Union Street<br>Burlington, Vermont 05401<br>(Asst. Director and Nursing Instructor, Fanny Allen Memorial School of Nursing)<br>Plattsburgh AFB |

*Atch 4*

## Page 64

Miss Harriet Miller (California Address: Post Office Box 565
Post Office Box 1019 Santa Barbara, California 93102)
Helena, Montana 59601
(Prominent in the field of
Education)
Malmstrom AFB

Mrs. John D. Montgomery (Mary E.)
424 Eisenhower Drive
Junction City, Kansas 66441
(Columnist, Junction City Daily Union Inc.)
Forbes AFB

Mrs. Gordon P. Oates (Will Etta)
485 Valley Club Circle
Little Rock, Arkansas 72207
(1st Vice-President, Arkansas Federation
of Women's Clubs, Public Relations work
and Commercial Advertising)
Little Rock AFB

Mrs. Forrest M. Pickett (Florence M.)
2805 S. W. Rutland Terrace
Portland, Oregon 97201
(Woman's Editor, Radio/TV)
McChord AFB

Mrs. Mamie B. Reese
614 Whitney Avenue
Albany, Georgia 31701
(Associate Professor of Education, and
Dean of Women, Albany State College)
Robins AFB

Dr. Hope S. Ross (Mrs. George T.)
1101 East Broadway
Enid, Oklahoma 73701
(Medical Doctor)
Vance AFB

Mrs. Thomas E. Sheppard (Eleanor P.)
1601 Princeton Road
Richmond, Virginia 23227
(Member, House of Delegates, Virginia
General Assembly)
Langley AFB

Miss June Strelecki
2 Berkeley Terrace 17B
Irvington, New Jersey 07111
(Lawyer - Private Practice)
McGuire AFB

2

## Page 65

Revised - April 1970

### MEMBERSHIP ROSTER
### DEFENSE ADVISORY COMMITTEE ON WOMEN IN THE SERVICES

**Appointed in 1969**

| | |
| :--- | :--- |
| Mrs. Beverly K. Bain<br>1363 Pleasant Valley Way<br>West Orange, New Jersey 07052<br>(Occupational Therapist)<br>McGuire AFB | Mrs. Helen K. Leslie *Handwritten: ABAC*<br>Box 13221<br>St. Petersburg, Florida 33733<br>(Executive Vice President, K & W<br>Supply House, Inc., (Co-owner)<br>and Civic Leader)<br>MacDill AFB |
| Dr. Loretta C. Ford<br>3040 5th Street<br>Boulder, Colorado 80302<br>(Professor, Public Health<br>Nursing, School of Nursing,<br>University of Colorado)<br>Lowry AFB | Mrs. Wray B. Lindersmith<br>4000 Massachusetts Avenue, N.W.<br>Washington, D. C. 20016<br>(Director of Sales and Public<br>Relations, Hotel Washington)<br>Andrews AFB |
| Mrs. Wilma D. Higginbotham<br>1831 Oak Ridge Drive<br>Charleston, West Virginia 25311<br>(Women's Editor - Charleston<br>Daily Mail)<br>Lockbourne AFB | Mrs. Myrtle W. Ollison<br>5101 North Everest Street<br>Oklahoma City, Oklahoma 73111<br>(Civic Leader)<br>Tinker AFB |
| Miss Katherine S. Horkan<br>50 Park Avenue<br>New York, New York 10016<br>McGuire AFB<br>Town Center Plaza<br>1000 6th Street, S.W.<br>Washington, D. C. 20024<br>(Co-Founder and Executive Vice<br>President of Communications<br>International, Inc.) | Mrs. Richard A. Sutter (Betty) *Handwritten: AJAD*<br>7215 Greenway Drive<br>St. Louis, Missouri 63130<br>(Civic Leader and an Editor of<br>Publications)<br>Scott AFB |
| Dr. Rachel M. Ice Hubbard<br>2611 Charing Road, Apt. B<br>Columbus, Ohio 43221<br>(Chairman, Food and Nutrition<br>Division, Ohio State University)<br>Lockbourne AFB | Mrs. Donna H. Tibbetts *Handwritten: ZIAD*<br>32 Norway Road<br>Bangor, Maine 04401<br>(Registrar, Beal College)<br>Pease AFB |
| *Handwritten: [The following entry is struck through with a horizontal line]*<br>Mrs. Geri Joseph<br>5 Red Cedar Lane<br>Minneapolis, Minnesota 55410<br>(Vice Chairman, Democratic<br>National Committee) | Mrs. Kris Anne Vogelpohl *Handwritten: AGAD*<br>8 Adler Circle<br>Galveston, Texas 77550<br>(Civic Leader)<br>Ellington AFB |
| | Dr. Norma B. Walker<br>2413 Alcoa Highway, S.W.<br>Knoxville, Tennessee 37920<br>(Pediatrician - Private Practice)<br>Arnold AFS |
| | Dr. Mary S. Zink<br>29 College Heights<br>Orono, Maine 04473<br>(Dean of Freshmen and Professor<br>of Education, University of Maine)<br>Pease AFB |

## Page 66

<p align="right">Revised - May 1970</p>

<p align="center">
MEMBERSHIP ROSTER<br>
DEFENSE ADVISORY COMMITTEE ON WOMEN IN THE SERVICES<br><br>
Appointed in 1970
</p>

| | |
| :--- | :--- |
| Mrs. William J. Bell (Lee Phillip)<br>209 East Lake Shore Drive<br>Chicago, Illinois 60611<br>(Television Personality, WBBM-TV)<br>Chanute AFB | Mrs. Elly M. Peterson<br>1625 Eye Street, N. W.<br>Washington, D. C. 20006<br>(Assistant Chairman, Republican<br>National Committee)<br>Bolling AFB |
| Mrs. Vivien Davenport<br>1500 Mims Street, S.W.<br>Atlanta, Georgia 30314<br>(Librarian, Atlanta Public Schools)<br>Dobbins AFB | Mrs. Catherine C. Ritchie<br>35 Hundreds Road<br>Wellesley Hills, Massachusetts 02181<br>(Educator and Civic Leader)<br>L. G. Hanscom Field |
| *Handwritten: bracket in left margin*<br>Mrs. Marcia Ellingson<br>3940 East Avenue<br>Rochester, New York 14618<br>(Civic Leader)<br>Hancock Field | Mrs. Estelle M. Stacy<br>#3 Hilltop Road<br>Post Office Box 96<br>Douglas, Wyoming 82633<br>(President, Stacy Drilling Company)<br>Francis E. Warren AFB |
| Mrs. Ellen K. Frautschi<br>3206 Lake Mendota Drive<br>Madison, Wisconsin 53705<br>(Research Assistant, University<br>Hospitals, Department of Pediatrics)<br>Gen Billy Mitchell Field | Mrs. Mary M. Stokes<br>275 Carolina Avenue, N. E.<br>Orangeburg, South Carolina 29115<br>(Civic Leader)<br>Shaw AFB |
| Mrs. Marilyn S. Fusfield<br>42 Riverview Heights<br>Sioux Falls, South Dakota 57105<br>(Civic Leader)<br>Offutt AFB | Miss Marie Torre (Mrs. H. M. Friedman)<br>57 Rocklynn Place<br>Pittsburgh, Pennsylvania 15228<br>(News Reporter & Hostess of TV<br>Show "Contact", KDKA-TV)<br>Greater Pittsburgh Airport |
| Mrs. June N. Gibbs<br>163 Riverview Avenue<br>Middletown, Rhode Island 02840<br>(Civic Leader)<br>L. G. Hanscom Field | Dr. Virginia Y. Trotter<br>2747 Woodsdale<br>Lincoln, Nebraska 68502<br>(Associate Dean, College of Agricul-<br>ture & Director, School of Home<br>Economics, University of Nebraska)<br>Offutt AFB |
| Mrs. Virginia B. Kenney<br>Route 2, Box 179A<br>Barrington, Illinois 60010<br>(Civic Leader)<br>Gen Billy Mitchell Field | Miss Antonina P. Uccello<br>207 Branford Street<br>Hartford, Connecticut 06112<br>(Mayor, City of Hartford)<br>Westover AFB |
| Miss Helen Lundstrom<br>125 East 2nd, North<br>Logan, Utah 84321<br>(Dean of Women and Director,<br>University Center, Utah State Univ.)<br>Hill AFB | |

## Page 67

Revised - May 1970

DEFENSE ADVISORY COMMITTEE ON WOMEN IN THE SERVICES

BIOGRAPHICAL INFORMATION
ON MEMBERS APPOINTED IN 1970

*Handwritten: A large "X" is drawn across the following two entries.*

<u>Mrs. William J. Bell (Lee Phillip), 209 East Lake Shore Drive, Chicago, Illinois 60611</u>

Native of Chicago, Illinois. Graduated Northwestern University (B.S.)
Business and Professional Affiliations: Director, Chicago Maternity
Center; Past President and Director, Chicago Unlimited; Director,
Academy of Television Arts and Sciences; Director, United Cerebral
Palsy; Director, Chicago Heart Association; Director, Newberry
Avenue Settlement House; Member, American Women in Radio and
Television; - and Fashion Group of America.
Mrs. Bell, known professionally as Lee Phillip, is a television per-
sonality on CBS-WBBM-TV in Chicago, Illinois.

<u>Mrs. Vivien H. Davenport, 1500 Mims Street, S.W., Atlanta, Georgia 30314</u>

Native of Washington, Georgia. Graduated Morris Brown College
(B.S.); Atlanta University (M.S.L.S. and M.A. equivalent).
Member: Board of Directors, Association for the Blind; Alpha
Kappa Alpha Sorority; National Education Association; Georgia
Teachers and Education Association; Atlanta Teachers Association;
Atlanta Library Association.
Business and Professional Affiliations: Atlanta Public Schools;
Visiting Professor, Library Science Department, Albany State College,
1962; Georgia Special State Reading Program, 1964; Adult Education
Affiliate; Director, ABE Night School Program.
Mrs. Davenport is a Librarian for the Atlanta Public Schools.

*Handwritten: The following entry is enclosed in large brackets on the left and right.*

<u>Mrs. Marcia Ellingson, 3940 East Avenue, Rochester, New York 14618</u>

Native of Newton, Massachusetts. Graduated Ohio State University
(B.S.).
Member: Board member, Hochstein Memorial Music School; Health
Assocation of Rochester & Monroe County, Tuberculosis Prevention
Committee, 1943-53; Division Chairman, 1936 and Board Member,
1939-43, Rochester Civic Music Association; Board Member, League

## Page 68

*Handwritten: A large circle is drawn around the following section:*

<u>Mrs. Marica Ellingson (cont'd)</u>

of Women Voters (Board Member 1937-42); Chairman & Radio Publicity, American Red Cross, Blood Donor Service, 1941-42; Monroe County League for Planned Parenthood; Rochester Museum Association, Women's Council; American Association of University Women; Century Club; Founder and Past Board Member, Genesee Figure Skating Club; Board of Directors; Ars Antiqua; Honorary Chairman, Rochester Report on Job Horizons for Women Workshop of the Women's Council of the State of New York, Department of Commerce, 1962; President and Founder, "Woman Power".
<u>Business and Professional Affiliations:</u> Founder and Honorary President (1960) Rochester Institute of Technology Women's Club; Founder and Honorary Member (1965), Rochester Institute of Technology Women's Council; Member, sub-committee on Housing and Student Services Committee-New Campus Planning, 1965-66.
<u>Awards:</u> Civic Achievement Award - Rochester Federated Women's Clubs, 1963; 1967 Civic Award, Susan B. Anthony Republican Club; Governor Rochefeller's Roster of Outstanding Women, 1968.
Mrs. Ellingson is a Civic Leader.

*Handwritten: A large 'X' is drawn through the following two sections:*

<u>Mrs. Ellen K. Frautschi, 3206 Lake Mendota Drive, Madison, Wisconsin 53705</u>

Native of Madison, Wisconsin. Graduated University of Wisconsin (B.S.).
<u>Member:</u> Board Member, Madison Art Association; Madison Civic Music Assocation; Madison General Hospital Auxiliary (Board Member 1962).
Mrs. Frautschi is a Research Assistant, University Hospitals - Department of Pediatrics, Madison, Wisconsin.

<u>Mrs. Marilyn S. Fusfield, 42 Riverview Heights, Sioux Falls, South Dakota 57105</u>

Native of Sioux Falls, South Dakota. Graduated Bowling Green State University of Ohio (B.S.).
<u>Member:</u> Vice President, Family Service Board; Leader, Girl Scouts-Children's Home, 1949-56; Counselor and Member, Girl Scout-Board, 1956-62; Painter and Promoter, Civic Fine Arts; President, P.T.A. Garfield Elementary School, 1965; President, Sioux Falls Pan Hellenic, 1958; Delta Gamma National Social Fraternity, YWCA; Rotary Ann.

2

## Page 69

<u>Mrs. Marilyn S. Fusfield (cont'd)</u>

<u>Business and Professional Affiliations:</u> Veteran's Administration, 1946-47.
Mrs. Fusfield is a Civic Leader.

<u>Mrs. June N. Gibbs, 163 Riverview Avenue, Middletown, Rhode Island 02840</u>

Native of Newton, Massachusetts. Graduated Wellesley College (B.A.) and Boston University (M.A.).
<u>Member:</u> Past President, Newport County Branch-American Association of University Women, 1954-56; Past President, Newport County Council of United Church Women, 1952-56; Past Vice President, Rhode Island Council of United Church Women, 1954-57; Past Vice Chairman, Rhode Island Republican State Central Committee, 1960-69; Preservation Society of Newport County; Board of Directors, Newport Historical Society, 1963-69; Navy League.
<u>Business and Professional Affiliations:</u> Naval Ordinance Division of Eastman Kodak, 1947-49.
Mrs. Gibbs is a Civic Leader.

<u>Mrs. Virginia B. Kenney, Route 2, Box 179A, Barrington, Illinois 60010</u>

Native of Evanston, Illinois. Graduated University of Chicago (Ph. B.).
<u>Member:</u> Organizing member and member of the Steering Committee of the Hyde Park-Kenwood Community Conference and area chairman of block organization; Women's Board of the National Conference of Christians and Jews, 1954-60; Governing Board of the Hyde Park Neighborhood Club, 1956-57; Board Member, Twenty-Ninth Ward Family Center; Scout Day Camp Organizer, 1957-58; Member, Board of Directors, Mother's Club Countryside School, Barrington, 1959-65; Secretary, Fox River Valley Pony Club, 1964-67.
<u>Business and Professional Affiliations:</u> Procurement Expediter for the Manhattan Project of the Atomic Energy Commission (University of Chicago), 1943-44; Finance Chairman, National Federation of Republican Women.
Mrs. Kenney is a Civic Leader.

3

## Page 70

**<u>Miss Helen Lundstrom, 125 East 2nd, North, Logan, Utah 84321</u>**

Native of Logan, Utah. Graduated Utah State University (B.S.);
University of Denver (M.B.A.).
Member: Business and Professional Women's Association; American
Association of University Women; Faculty Women's League; University
Women's Club; Adviser, Building Corporation Chairman and Treasurer,
Alpha Chi Omega.
Business and Professional Affiliations: President, Lundstrom Furni-
ture Company; Business Education Associations (Utah - Director,
1960-62; Western - Secretary, 1959, 1964 and Treasurer, 1965;
National - Regional Membership Chairman, 1959-60); Assistant
Professor, Faculty Association Officer and member of numerous
committees, Utah State University; Phi Kappa Phi, (Chapter Secretary
1959-61); Mortar Board, Honorary Member, 1970; Delta Pi Epsilon,
(Chapter President 1957); Alpha Lambda Delta; National Association
of Women Deans and Counselors; Utah Association of Women Deans
and Counselors; American Guidance and Personnel Association;
American College Personnel Association; Utah College Personnel
Assocation.
Miss Lundstrom is Dean of Women and Director of University Center,
Utah State University, Logan, Utah.

**<u>Mrs. Elly M. Peterson, 1625 Eye Street, N.W., Washington, D.C. 20006</u>**

Native of New Berlin, Illinois. Attended William Woods College,
Northwestern University and Suburban Business College.
Member: American Legion Auxiliary; Urban League; Cosmopolitan
Business and Professional Women's Club.
Business and Professional Affiliations: Republican State Vice Chairman
(Michigan), 1961-63; Assistant Chairman, Republican National Committee,
1963; Republican State Chairman (Michigan), 1965-69.
Mrs. Peterson is the Assistant Chairman, Republican National
Committee.

**<u>Mrs. Catherine C. Ritchie, 35 Hundreds Road, Wellesley Hills,</u>**
**<u>Massachusetts 02181</u>**

Native of Wheeling, West Virginia. Graduated Smith College (A.B.
cum laude); Cornell University (M.A.); attended West Liberty Normal
School, Wilsons Teacher's College, Catholic University, Boston
University, and Wellesley College.

4

## Page 71

**Mrs. Catherine C. Ritchie (cont'd)**

Member: Board of Directors, Eastern Branch, YMCA, 1950-60; Corresponding Secretary, Southeast Business and Professional Women's Club, 1956-58; Life Member, Soroptimist Club of Washington, D. C. (President 1958-59); Washington, D. C. Board of Trade, 1959-60; Peace Corps, Volunteer--Nigeria, 1961-63; Volunteer for Better Schools in Boston, 1965-67; Friendly Visitor, Massachusetts Correctional Institute, Framingham, Massachusetts, 1968-69; Life Member, D. C. Congress of Parents & Teachers; Smith College Club of Washington, D. C., 1931-64 (Chairman of Scholarships 1944-46); The Wellesley Smith Club, Massachusetts, (Program Chairman 1967-69).

Business and Professional Affiliations: Principal, Kramer Junior High School, Washington, D. C., 1946-64; Member-Treasurer-Secretary-Chairman of Board of Junior High School Principals, 1946-64; Recipient of Fulbright Grant to teach in Adisadel College, Cape Coast, Ghana, 1953-55; Assistant to Dr. Babs Fafunwa, Head of Harden College of Education, University of Nigeria, 1961-63; Secretary to the Institute of Education of Eastern Nigeria, 1961-63; Director of Vacation School for elementary school teachers in Eastern Region, Nigeria, Summer 1962; Organizer of enrichment program for lecturers of Teachers Training Colleges of Eastern Nigeria, February 1963.

Mrs. Ritchie is an Educator and Civic Leader.

**Mrs. Estelle M. Stacy, #3 Hilltop Road, Post Office Box 96, Douglas, Wyoming 82633**

Native of Grimes County, Texas. Attended various colleges and universities.

Member: State Advertising Chairman for Wyoming Clubwoman for two years, Wyoming Federation of Women's Clubs; Past Matron and Past Grand Representative, Order of Eastern Star; Community Achievement Contest Chairman for Sears Roebuck for two years, Wyoming Federation of Women's Clubs; Board of Directors and Legislative Committee, Wyoming Safety Council; Past President, Douglas Civic Club; Douglas Chamber of Commerce; Douglas Country Club.

Business and Professional Affiliations: Vice President Stacy Drilling Company, 1948-63; Past Vice President and now President, Teno United (Wyoming Corporation); Legislative Chairman, Wyoming Drilling Association; Advisor, Douglas Development Association; Wyoming Taxpayers Association; Wyoming Retail Merchants Association; Treasurer, Converse County Foundation; President, Converse County Library Board of Trustees; Wyoming Flying Farmers.

Mrs. Stacy is President of the Stacy Drilling Company.

5

## Page 72

Mrs. Mary M. Stokes, 275 Carolina Avenue, N.E., Orangeburg, South Carolina 29115

Native of Chester, South Carolina.  Attended Winthrop College and Dora Ellis Business College.
Member: National Executive Committee, American Legion Auxiliary; Past President, American Legion Auxiliary, South Carolina; Chairman, Americanism, American Legion Auxiliary, Southern Division; Director, American Cancer Society, South Carolina; Executive Board, State Mother Committee, South Carolina; Chairman and Director, Palmetto Girls State; President, American Legion Auxiliary, Orangeburg, 1964-65; President, Orangeburg Assembly, 1962-63; President, Tuesday Book Club, 1963-64; Treasurer, Orangeburg Garden Club, 1961-62; District Director, Episcopal Church Women, 1950-53; President, Episcopal Church Women, Orangeburg, 1949-50.
Mrs. Stokes is a Civic Leader.


Miss Marie Torre (Mrs. H. M. Friedman), 57 Rocklynn Place, Pittsburgh, Pennsylvania 15228

Native of New York City.  Graduated New York University (B.A.).
Member: Business and Professional Women's Association; Civic Light Opera Guild; Small Business Administration; American Federation of TV and Radio Artists.
Business and Professional Affiliations: Television Columnist, New York Herald Tribune; Reporter-Editor, New York World-Telegram and Sun.
Awards: Distinguished Service Award from the Italian Sons and Daughters of America; Variety Club's (Tent #1) Red Rose Award; Professional Awards from the Syracuse Press Club, the American Jewish Congress, the Hudson County Press Club, the U. S. Army, the American Federation of TV and Radio Artists, the Business and Professional Women's Association, and three Woman of the Year Awards from the Lambs in New York.
Miss Marie Torre is a news reporter and hostess of television show "Contact", KDKA-TV, Pittsburgh, Pennsylvania.


6

## Page 73

**Dr. Virginia Y. Trotter, 2747 Woodsdale, Lincoln, Nebraska 68502**

Native of Boise, Idaho. Graduated Kansas State University (B.S. and M.S.); Ohio State University (Ph. D. ).
**Member:** Mortar Board; American Home Economics Association; President, Nebraska Home Economics Association; American Dietetic Association; Nebraska Dietetic Association; American Association of University Women; ALTRUSA; Omicron Nu; Phi Upsilon Omicron; Alpha Delta Pi; International Rehabilitation Society; International Home Economics Association; Nebraska Rehabilitation Society; Nebraska Heart Association Board; President's Committee on Employment of the Handicapped (Chairman, Homemaker Rehabilitation sub-group); Advisory Council, New York State College of Human Ecology.
**Business and Professional Affiliations:** Instructor of Home Management, University of Utah, 1948-50; Assistant Professor and Head of Department of Family Economics and Management, University of Nebraska, 1950-55; Assistant Dean, College of Agriculture and Home Economics and Chairman, Department of Home Economics, University of Vermont, 1955-63; Associate Director, Nebraska Experiment Station; Professor, Family Economics and Management, University of Nebraska. Dr. Trotter is Associate Dean, College of Agriculture and Director, School of Home Economics, University of Nebraska.

**Miss Antonina P. Uccello, 207 Branford Street, Hartford, Connecticut 06112**

Native of Hartford, Connecticut. Graduated St. Joseph College, (B.S.); attended Trinity College and University of Connecticut School of Law.
**Member:** American Association of University Women; League of Women Voters; Pilot Club; Past President, Alumnae Association of St. Joseph College; Past Secretary, Catholic Graduates Club of Greater Hartford.
**Business and Professional Affiliations:** Advisory Board, U.S. Conference of Mayors; Director, Connecticut Conference of Mayors; Vice Chairman, Executive Board--Regional Council of Elected Officials.
Miss Uccello is Mayor of the City of Hartford, Connecticut.

7

## Page 74

Revised - April 1970

DEFENSE ADVISORY COMMITTEE ON WOMEN IN THE SERVICES

BIOGRAPHICAL INFORMATION
ON MEMBERS APPOINTED IN 1969

**Mrs. Beverly K. Bain, 1636 Pleasant Valley Way, West Orange, New Jersey 07052**

Native of Colorado. Graduated from Trinidad Junior College (A.A.) (Outstanding Senior Women, Phi Theta Kappa Honorary); Colorado State College (B.A.) (Selected Women of Tomorrow); the University of Southern California (Certificate in Occupational Therapy); Warm Springs Georgia (Fellow in Polio); and the University of California at Los Angeles (Fellow in Prosthetics).
Member: American Occupational Therapy Association; Past President, New Jersey Occupational Therapy Association; Board Member in Charge of High School Volunteers, New Jersey Orthopaedic Hospital Auxiliary; Co-Chairman and Decoration Chairman, Cafe' Chantant (Funds for C. P. Reh. Institute); Fund Raiser for Orange Memorial Hospital, Funorama on Ice; Chairman of Community Affairs, Junior Women's Club of the Oranges.
Business and Professional Affiliations: Director of Physical Disability Section of Occupational Therapy, Los Angeles County Hospital; Director of Occupational Therapy, Kessler Rehabilitation Institute; Director of Occupational Therapy Rehabilitation Department of the New Jersey Orthopaedic Hospital; Cerebral Palsy Rehabilitation Institute; Perceptual Motor Dysfunction Unit of Hospital Center at Orange; Graduate Work, Montclair State College.
Publications: A.M.A. Journal, Co-Author Electrical Arm Slings; Co-Author of various films and publications on the training of Arm Amputees and "Stroke" patients with Doctor Kessler and Doctor Earl F. Hoerner.
Mrs. Bain is an Occupational Therapist (employed part time).

**Dr. Loretta C. Ford, 3040-5th Street, Boulder, Colorado 80302**

Native of New York. Diploma from Middlesex General Hospital; Graduated from the University of Colorado School of Nursing (B.S.); the University of Colorado School of Nursing (M.S.); and the University of Colorado School of Education (Ed. D.).
Member: Secretary-Treasurer, President, Colorado State Board of Nursing; Colorado State Board of Practical Nursing; Chairman, Public Health Nursing Section, American Public Health Association; American Red Cross Nursing Advisory; Board of Directors, Colorado Public Health Association; American Association of University Professors; American School Health Association; American Nurses Association, Nat'l League for Nursing; American Health Association (Fellow); and various other professional organizations.
Business and Professional Affiliations: Staff Nurse, Supervisor and Director of Nursing in Health Department; Staff, University of Colorado.
Dr. Ford is Professor of Public Health Nursing, University of Colorado.

## Page 75

Mrs. Wilma D. Higginbotham, 1831 Oak Ridge Drive, Charleston, West Virginia 25311

Native of West Virginia. Attended Marshall University, Huntington, West Virginia and Columbia University.
Member: Alpha Iota Sorority, 1935-Honorary; President, Pilot Club of Charleston, West Virginia; Press Club of Charleston, West Virginia; Volunteer Hospital Aide, American Red Cross; West Virginia Press Association.
Business and Professional Affiliations: News Reporter, Charleston Gazette; Staff Member, West Virginia Review; Woman's Editor, Charleston Daily Mail.
Mrs. Higginbotham is a Woman's Editor - Charleston Daily Mail.

Miss Katherine S. Horkan, 50 Park Avenue, New York, New York 10016; Town Center Plaza, 1000 6th Street, S.W., Washington, D. C. 20024

Born - Paris, France. Graduated from Mount Vernon Seminary and Junior College, Washington, D. C.; University of Heidelberg; American University and the University of Maryland (overseas).
Member: Overseas Press Club of America; American Women in Radio and Television, New York and Washington, D. C. Chapters; Public Relations Society of America; National Federation of Business and Professional Women's Clubs; Union Club, Frankfurt, Germany; International Club, Washington, D. C.; Women's Advertising Club of Washington, D. C.; National Women's Republican Club, New York City; National Association of Educational Broadcasters.
Business and Professional Affiliations: Assistant to Director of Unit Publications, Troop Information and Education Division, USAREUR Headquarters, Heidelberg; Scenario - Film Writer, Armed Forces Pictorial Center; Travel Editor and Columnist, Overseas Weekly; Travel Editor, Columnist and Correspondent, Overseas Family; Public Relations Representative and Account Executive, Pan American Broadcasting Company and International Media Company, Inc.; Associate Editor, You and Europe magazine; Contributing Editor, Holland International; Associate Editor, Amsterdam Today; Manager, U. S. Department, Amsterdam Tourist Association; Writer and Broadcaster, Radio Netherlands; Director, Public Relations and Publicity, Oscar Film Company, Inc.; Director of Public Relations, International Travel Education Foundation; Director of Public Relations, The Marriott Corporation, Inc.; Media Director, Community Relations Division, Girl Scouts of the U.S.A.; Director of National Development, Girl Scouts of the U.S.A.; Director, Materials Production Division, Girl Scouts of the U.S.A.; member, Editorial Board Leader Magazine; Free Lance Writer - Photographer, New York Times, Washington Post, Algemeen Handelsblad (Holland), NEA Journal, The Quotarian, and Civitan Magazine.
Awards and Honors: Who's Who Overseas Press Club of America.
Miss Horkan is the Co-Founder and Executive Vice President of Communications International, Inc.

2

## Page 76

<u>Dr. Rachel M. Ice Hubbard, 2611 Charing Road, Apt. B, Columbus,</u>
<u>Ohio 43221</u>

Native of Ohio. Graduated from Ohio State University (B. S. ); Cornell University (M. S. ); and the University of Wisconsin (Ph. D. ).
<u>Member:</u> Board of Directors, Quota Club of Columbus, Ohio.
<u>Business and Professional Affiliations:</u> Chief, Food Technology Section, U. S. Air Force Services Division, Wright-Patterson AFB; Assistant Director for Administration, University Hospital, Ohio State University; Assistant Professor and Head, Institution Management, School of Home Economics, Ohio State University.
Dr. Hubbard is Chairman, Food and Nutrition Division, The Ohio State University.

*Handwritten: [A large 'X' is drawn across the following section for Mrs. Geri Joseph]*

<u>Mrs. Geri Joseph, 5 Red Cedar Lane, Minneapolis, Minnesota 55410</u>

Native of Minnesota. Graduated from the University of Minnesota (B. A. ).
<u>Member:</u> Advisory Council, National Institute of Mental Health; Appointed to the President's Committee on Youth Employment 1962 by President Kennedy; Chairman, on Permanent Organization, 1964 Democratic National Convention; Appointed to the President's Commission on Income Maintenance 1968 by President Johnson; National Committee Woman for Minnesota since 1960.
<u>Business and Professional Affiliations:</u> Former staff writer with the Minneapolis Tribune, 1946-1953.
<u>Awards and Honors:</u> Distinguished Service Award, Minnesota Junior Chamber of Commerce, 1952; Recipient of five American Newspaper Guild Awards.
Mrs. Joseph is Vice Chairman, Democratic National Committee and President, National Association for Mental Health.

<u>Mrs. Helen K. Leslie, 4035 Grove Street, South, St. Petersburg,</u>
<u>Florida 33705</u>
(Mailing Address: Box 13221, St. Petersburg, Florida 33733)

Native of New Jersey. Attended St. Petersburg Junior College and the University of Tampa. Graduated from Auburn University (B. S. ).
<u>Member:</u> Past President and other offices, Woman's Service League; Member, St. Petersburg AAA Traffic and Safety Committee; Served

3

## Page 77

<u>Mrs. Helen K. Leslie (cont'd)</u>

on Executive Committee - 2 years, Women's Conference, National Safety Council; Member since 1964, Chairman, May 67-October 68, Florida Commission on the Status of Women; Presided at First Conference of Business and Professional Women of the Americas, Puerto Rico - 1961; Past Chairman of Hemispheric Friendship Committee, involving trips into Central and Northern South America. Member since 1952, St. Petersburg Civil Defense Advisory Committee; Past Board Member, Present member nominating Committee, Young Women's Christian Association (YWCA); Board Member, Vice President, Police Athletic League; Chairman, Delta Zeta Sorority; Mortar Board (College Honorary).

<u>Business and Professional Affiliations:</u> Member, Research and Education Committee, Business and Professional Women's Foundation; Member, Pinellas County General Advisory Committee for Vocational, Technical and Adult Education; Past State President, Florida Business and Professional Women's Club, Inc.; Past National President, National Federation of Business and Professional Women's Clubs, Inc.

Mrs. Leslie is Executive Vice President - Co-owner - K & W Supply House, Inc. and a Civic Leader.

<u>Mrs. Wray B. Lindersmith, 4000 Massachusetts Avenue, N. W.</u>
<u>Washington, D. C. 20016</u>

Native of North Carolina. Attended Miami University and Houston University.

<u>Member:</u> Committee Chairman, Sales and Marketing Executives of Washington, D. C. Inc.; Washington, D. C. Chapter, Hotel Sales Management Association; Women's Advertising Club of Washington, D. C.; Texas State Society; Dallas, Texas, Hotel Sales Management Association; Ligonier Valley Garden Club, Pennsylvania; Southern Club, Pittsburgh, Pennsylvania; Pittsburgh Athletic Association; Pittsburgh Field Club.

<u>Business and Professional Affiliations:</u> Sales and Public Relations, Baker Hotel, Dallas, Texas; Career Advisory Board, Sanger Harris, Dallas, Texas; Co-owner of Ken Buick, Inc., and Keystone Auto Rental, Pittsburgh, Pennsylvania.

<u>Awards and Honors:</u> Raymond Bill Award -- Committee Chairman, Sales and Marketing Executives of Washington, D. C. Inc.

Mrs. Lindersmith is Director of Sales and Public Relations, Hotel Washington, Washington, D. C.

<u>Mrs. Myrtle W. Ollison, 5101 North Everest Street, Oklahoma City,</u>
<u>Oklahoma 73111</u>

Native of Texas. Attended Prairie View College. Graduated from Langston University (B. S.); the University of Cincinnati and the University of Oklahoma (M. A.).

4

## Page 78

<u>Mrs. Myrtle W. Ollison (cont'd)</u>

Member: President, National Association Colored Women's Clubs, Inc.; President, Southwest Region, National Association Colored Women's Clubs; Vice Chairman, Oklahoma Minority Group; American Association of University Women; Member, Women for Nixon-Agnew. National Advisory Committee; President Du Bois Study Club; Director of Music, Baptist Church, Shawness, Oklahoma; Delta Sigma Theta Sorority; National Phi Delta Kappa Sorority.

Business and Professional Affiliations: Teacher, City Schools, Shawnee, Oklahoma; Chairman, Reading Committee, Horace Mann School, Shawnee; Member, Oklahoma Manpower Advisory Committee.

Awards and Honors: Honorary Lieutenant Governor, Oklahoma.
Mrs. Ollison is a Civic Leader.

<u>Mrs. Elizabeth H. Sutter, 7215 Greenway Drive, St. Louis, Missouri 63130</u>

Native of Missouri. Graduated from Washington University (A.B.).
Member: President, Woman's Auxiliary to the American Medical Association; Chairman, St. Louis County Health and Hospital Advisory Board; Chairman, Citizen's Committee (successful in securing passage of legislation for fluoridation of water supply); 10 year member, Planning Board, Health and Hospital Division, Health and Welfare Council of Metropolitan St. Louis; Chairman, Practical Nurse Education Council; Advisory Committee, Deaconess Hospital School of Nursing; President, three terms, St. Louis Tuberculosis and Health Society (only woman in this capacity in 64 years); Board, St. Louis Unit of the American Cancer Society; Board, Mental Health Association of St. Louis; Advisory Council on the Volunteer National Association for Mental Health; Finance Chairman, six years, Women's Association, First Presbyterian Church of St. Louis; Vice President, Board of Trustees, John Burroughs School, St. Louis; Appointed in 1957 by the St. Louis County Council as member, Historic Buildings Commission; President, Century Club Arts and Sciences Alumni, Washington University; Board, Alumni Federation, Washington University; Secretary-Treasurer, Board of Directors, Sutter Clinc, Inc., St. Louis.
Business and Professional Affiliations: Contributor to publications: <u>Missouri Medicine, MD's Wife</u>; Editor, Direct Line Newsletter of the American Medical Association Auxiliary.

Awards and Honors: St. Louis Globe-Democrat, Woman of Achievement, 1961; St. Louis County Medical Society Award of Merit, 1964; Honor Guest, St. Louis Alumnae of Gamma Phi Beta, 1966; Alumni Citation, Washington University, 1968. Listed in <u>Who's Who of American Women</u> and <u>Who's Who in the Midwest.</u>
Mrs. Sutter is a Civic Leader and an Editor of Publications.

<center>5</center>

## Page 79

<u>Mrs. Donna H. Tibbetts, 32 Norway Road, Bangor, Maine 04401</u>

Native of Maine. Attended Husson College, and the University of Connecticut. Presently attending the University of Maine.
Member: Secretary, Republican City Committee; State Govenment Chairman, League of Women Voters; Treasurer, Penobscot Women's Republican Club; Treasurer, Maine Federation of Republican Women.
Business and Professional Affiliations: Private Secretary, Kagan Lown and Company, Bangor, Maine: Treasurer, Bangor Data Processing.
Mrs. Tibbetts is the Registrar, Beal College, Bangor, Maine.

<u>Mrs. Kris Anne Konugres Vogelpohl, 8 Adler Circle, Galveston, Texas 77550</u>

Native of Colorado. Graduated from Colorado State University (B. S.); American Dietitic Association, Dietitic Internship, University of Colorado Medical School (Outstanding Intern in the Class).
Member: Delegate to International Conference in Rome, 1956 American Dietitic Association; President, New Mexico, Dietitic Association; Texas, Dietitic Association; National Committeewoman, Young Republicans; President, Vice-President, Secretary, President-Elect, Woman's Auxiliary to Galveston County Medical Society; Delegate to National Convention, State Public Relations Chairman, Woman's Auxiliary to Texas Medical Society; Vice President, American Association of University Women; Trinity Episcopal School Board; Vice-President, Galveston County Mental Health Board of Directors; Vice-President and president, Philaptohos (Women of Church); District 16 Secretary, 1963 International Daughter of the Year, Daughters of Penelope; Nominating Committee, Southern Texas Girl Scouts of America Council; Salvation Army; President, Young Women's Christian Association; Chamber of Commerce Polution Board (Only woman on a 35 member board); Chamber of Commerce Oceanography Board; Governor Smith's Committee on Children and Youth.
Business and Professional Affiliations: Staff Dietician, University of Colorado Medical School; Head Dietician, Atomic Energy Commission; Chief, Therapeutic Dietician, University of Texas Medical Branch, Instructor in Nutrition, University of Texas Medical Branch.
Mrs. Vogelpohl is a Civic Leader.

<u>Dr. Norma B. Walker, Alcoa Highway, Knoxville, Tennessee 37920</u>

Native of Tennessee. Graduated from the University of Tennessee (B. S.); the University of Tennessee, College of Medicine (M. D.); Internship, Medical College of Virginia; Pediatric Residence - 1956-57; Pediatric Residency, Vanderbilt University Hospital - 1957-58.

<p align="center">6</p>

## Page 80

<u>Dr. Norma B. Walker (cont'd)</u>

<u>Member:</u> Tennessee Society of Pediatrics; Tennessee Medical Association; Knoxville Academy of Medicine; American Medical Association; American Academy of Pediatrics.
<u>Business and Professional Affiliations:</u> Public Health Office, Lincoln-Moore Giles Counties, Tennessee; Children's Hospital, Cincinnati, Ohio; Staff member of five hospitals in Knoxville.
Dr. Walker is a Pediatrician. (Private Practice).

<u>Dr. Mary S. Zink, 29 College Heights, Orono, Maine 04473</u>

Native of Connecticut. Graduated from Cornell University (A. B.); Yale University (M. A.); and Cornell University (Ph. D.).
<u>Member:</u> President, Chairman, Higher Education Committee and Area Representative - Education, American Association of University Women, Orono - Old Town Branch; Treasurer, Alamance County Branch, American Association of University Women; Program Chairman, Durham, North Carolina, American Association of University Women; Board of Directors and Chairman, Education Committee, Dunkirk-Fredonia Branch, Batavia, New York, American Association of University Women; Selection Panel for Region I USOE Fellows Program 1969; National Association Girl Scout Executives; Business and Professional Women's Club, Zonta, Altrusa; various regional committees and offices.
<u>Business and Professional Affiliations:</u> National Association, Deans and Counselors; Nominating Committee and National Advisory Committee, Intercollegiate Association, Women Students; Vice President and President, Maine Association, Women Deans and Counselors; Chairman, Education Committee, North Carolina Association, Women Deans and Counselors; American Psychological Association; Maine Psychological Association; American College Personnel Association; National Vocational Guidance Association.
Dr. Zink is Dean of Freshmen and Professor of Education, University of Maine.

7

## Page 81

Revised - April 1970

DEFENSE ADVISORY COMMITTEE ON WOMEN IN THE SERVICES

BIOGRAPHICAL INFORMATION
ON MEMBERS APPOINTED IN 1968

<u>Mrs. Celia Aidinoff, 110 East End Avenue, New York, N. Y. 10028</u>

Native of New York City. Graduated Agnes Scott College (B. A.).
Member: Board of Directors, Executive Committee and Chairman Public Relations Committee, International Center in New York; Executive Committee, Women's Division, Legal Aid Society; Executive Committee and Editor of Curtaincalls, Friends of the City Center of Music and Drama; Public Relations Committee, Women's Africa Committee; Associates Committee, Institute of International Education; New York City Commission to the United Nations; Off-the-Record Luncheons, Foreign Policy Association; St. Bernard's School Representative of the Independent Schools Committee, Public Education Association; Northeast Regional Vice President and President of New York City Chapter, Agnes Scott College Alumnae Association.
Business and Professional Affiliations: Editor of Publications, Institute of International Education; Editor of Publications, Near East College Association; Editorial Assistant, Consumer Reports; Assistant Public Relations Officer, Pakistan Mission to the United Nations; Volunteer Editorial Work, United Nations Association.
Mrs. Aidinoff is an Editor of Publications, Public Relations Director and a Civic Leader.

<u>Mrs. Marian C. Atkinson, 2560 North Summit, Milwaukee, Wisconsin 53211</u>

Native of Pennsylvania. Attended Howard University, St. Louis University and the University of Wisconsin.
Member: Chairman, Housing Committee 1959-63; League of Women Voters; Chairman, East Side High School Group, American Field Service Council; Chairman, Milwaukee Hostesses for NMA: Chairman, Adoptive Homes Program, Community Welfare Council; Chairman, East Side Girl Scout Council; YWCA Speaker's Bureau; Women's Auxiliary to Abdominal Surgeons; President, 1955-57-59 Beta Tau Chapter, Delta Sigma Theta National Sorority.
Business and Professional Affiliations: Occasional writer and journalist. Teacher in the Social Improvement Program, Milwaukee School Board.
Mrs. Atkinson is a teacher in the Social Improvement Program, Milwaukee School Board and an occasional writer.

## Page 82

**Mrs. Jeraldine J. Bostwick, 2259 Kalakaua Ave., Honolulu, Hawaii 96815**

Native of Portland, Oregon. Graduated from Colorado Women's College (B.S.) and the University of Washington (Bachelor of Journalism).
**Member:** Honolulu Press Club; Oahu Country Club; Outrigger Canoe Club; Vice President, Honolulu Public Relations Association; President, Hawaii Chapter, Public Relations Society of America; Board of Directors Honolulu Community Theatre; Board of Directors, WAIF-ISS; Public Relations and Publicity Boy Scout Makahikis; President Hawaii Chapter, Theta Sigma Phi.
**Business and Professional Affiliations:** Director of Public Relations, Matson Hotels, Hawaii; Director of Public Relations and Advertising, Greenbrier Hotel; Director Public Relations and Advertising, Sheraton-Hawaii Corp.
Mrs. Bostwick is Director of Public Relations and Advertising, Pacific Area, Sheraton Hawaii Hotel Corporation.

**Mrs. Margaret Elizabeth Boyd, 746 North Xenophon, Tulsa, Oklahoma 74127**

Native of Tulsa, Oklahoma. Attended the University of Tulsa; Iowa State University and is currently working toward teaching certification at the University of Tulsa.
**Member:** Women's Division Director, Tulsa and National Publicity Committee, National Foundation, Crippled Children's Foundation; Tulsa City-County PTA; Tulsa County Council for Mentally Retarded; Gatesway Foundation; Cerebral Palsy Association Senior Board; Dance Showcase of Tulsa, Board of Management, Westside YMCA; Board Member, Family and Children's Service; Board Member, Tulsa Area Safety Council; Delta Delta Delta Sorority; Pi Delta Epsilon, Journalism Honorary; Who's Who of American Women; Who's Who in Tulsa; Who's Who in the Southwest; **International Dictionary - London;** American Women in Radio and Television - Awarded "Golden Mike" 1967 (one of 7 given in the U.S.)
**Business and Professional Affiliations:** Woman's Director and Broadcaster, KOTV.
Mrs. Boyd is Broadcaster - Woman's Editor and Director of Public Service, Griffin-Leake TV (KTUL-TV).

**Mrs. C. Wayland Brooks, 1110 Watergate, West, Washington, D. C. 20037**

Native of Colby, Kansas. Attended Mills College, Oakland, Calif.; University of Idaho (B.A.).
**Member:** Kappa Kappa Gamma; AAUW; American Legion Auxiliary; Vice Chairman of Red Cross District (local); Mental Health Board; Immigrant Service League; Illinois Children's Home and Aid; Light House for the Blind; Arden Shore Assoc.; Board of Illinois State Federation of Republican Women.

2

## Page 83

83201
```

No, that's too much. I'll just use plain text.

Final decision: Bold for underlined headers, plain text for the rest.

```markdown
**Mrs. C. Wayland Brooks (continued)**

Became a member of the Republican National Committee in 1957 and in 1960 was elected Vice Chrm. Served as official hostess to the Republican National Convention, Chicago in 1960 and as Vice Chrmn. of the Committee on Big City Politics in 1961. Resigned from the Republican National Committee in 1963 and returned to Idaho. Was appointed Assistant Chairman of the Republican National Committee in 1965.
Mrs. Brooks is the widow of the former U. S. Senator C. Wayland Brooks from Illinois. Mrs. Brooks is Superintendent, U. S. Mint.

**Mrs. Janell S. Burke, Dean of Women, Idaho State University, Pocatello, Idaho**
                                                                        83201

Native of Caldwell, Idaho. Graduated: The College of Idaho (B. A. in Piano); Indiana University (M. S. in Education).
Member: National Association of Women Deans and Counselors; Governor's Commission on the Status of Women, State of Idaho; American Association of University Women; Faculty Women's Club, Idaho State University; Idaho Personnel and Guidance Association.
Business and Professional Affiliations: Private Piano teacher, Resident Assistant, Indiana University; Director of Choral Music, Jermoe Public School System, Jermoe, Idaho; Assistant Head Counselor, Indiana University; Assistant Dean for Women, Idaho State University; Associate Dean for Women, Idaho State University.
Mrs. Burke is Dean of Women, Idaho State University.

**Miss Elaine Burnham, 255 S. W. Harrison Street, Apt 2F, Portland, Oregon 97201**

Native of Oregon City, Oregon. Attended the University of Oregon.
Member: Business and Professional Women's Auxiliary, Portland Symphony Association; Executive Board, Assistant Treasurer Oregon Telephone Employees Credit Union; Chairman of Credit Commission, Oregon Division; Secretary-Treasurer, Communications Workers of America; Key (United Good Neighbors Volunteers).
Miss Burnham is Facilities Supervisor for the Pacific Northwest Bell Telephone Company.

**Mrs. Helen H. Cannon, 108 South Izard Street, Forrest City, Arkansas 72335**

Native of Arkansas. Attended Ouachita Baptist University and Arkansas State College, (L. I.).
Member: Chairman, Forrest City Centennial Committee; First President and Organizer, St. Francis Historical Society; Co-Chairman and Organizer, Arkansas Women's Council; Member, Board of Directors, Arkansas Training School for Girls at Fargo, Ark.; Governor's Commission on Migratory

                                  3
```

Wait, I'll just use plain text for everything to be as "clean" as possible.

```markdown
Mrs. C. Wayland Brooks (continued)

Became a member of the Republican National Committee in 1957

## Page 84

Mrs. Helen H. Cannon (continued)

Labor; Chairman, Cultural Heritage Division, General Federation of Women's Clubs; Chairman of Community Improvement Program of General Federation of Women's Clubs and Sears Roebuck Foundation; served as President, 1st and 2nd Vice President and Treasurer, Arkansas Federation of Women's Clubs; General Federation of Women's Clubs; Hostess, Old State House, Little Rock; Vice President, Nathan Bedford Forrest Chapter of United Daughters of the Confederacy; Vice President, Parent-Teachers Assoc.; Memphis Rose Society; Girl Scout Troop Leader; Listed in Who's Who of American Women.

Business and Professional Affiliations: Legal Secretary, Carroll C. Cannon, Attorney, St. Louis, Missouri and Forrest City, Arkansas; Legal Secretary, Reconstruction Finance Corp; Legal Secretary, The Federal Land Bank of St. Louis.

Mrs. Cannon is co-owner of the St. Francis County Title and Abstract Company.

Dr. Helen E. Clarke, 3413 Duke Street, College Park, Maryland 20740

Native of Edmonton, Alberta, Canada. Graduated University of Michigan (B.S.); Mayo Clinic (Certificate Physical Therapy); University of Illinois (M.A.); Teachers College, Columbia University (Ed. D.). Members: Treasurer and National Membership Chairman, National Association of Women Deans and Counselors; Regional Association of Women Deans and Counselors; American Personnel and Guidance Association; American College Personnel Association; National Association of Student Personnel Administrators; National Education Association; American Association of University Women, Soroptimist International Association; Kappa Delta Pi; Lambda Theta; Sigma Delta Pi; Mortar Board (Honorary Membership); Alpha Lambda Delta (Honorary Membership); Who's Who in America; Who's Who in American Women; Who's Who in Education. Business and Professional Affiliations: Chairman, Subcommittee on Higher Education of the Governor's Commission on the Status of Women in Maryland; Member, Middle States Association Evaluation Team on Student Personnel Services to Rutgers University; Advisory Educational Policies Commission of the National Education Association and the American Association of School Administrators. Published Writing: "The Head Resident's Administrative and Student Government Relationships," Journal of the National Association of Women Deans and Counselors.

Dr. Clarke is Associate Dean of Students, University of Maryland.

## Page 85

Dr. Marjorie S. Dunlap, Dean, School of Nursing, Univ. of Calif. Medical Center,
3rd and Parnassus, San Francisco, California 94122
________________________________________________________________________________

Native of Kansas City, Missouri. Attended Washington University School
of Nursing (Diploma); University of Chicago (6 mos. Seminar in Nursing
Service Administration). Graduated from the University of Missouri (A. B.)
University of Colorado (Master of Personnel Service); University of
Southern California (Doctor of Education).
Member: American Nurses Association; National league for Nursing;
Hawaii Nurses Association; Hawaii League for Nursing; Secretary,
Colorado League for Nursing, 1948; Chairman, EACT Section, Colorado,
1953; Chairman, EACT Section, American Nurses Association 1953-54;
Board of Directors, California League for Nursing, 1963-64; Unit E
Board of Directors, California League for Nursing, 1963-64, 1964-65;
President, Hawaii Nurses Association 1967-68; Joint Committee on Uni-
fication of Accrediting Activities, National League for Nursing, 1950;
Committee on Bibliography for Nursing Service Administration, National
League for Nursing, 1957-58; Selective Service System -- National Advisory
Committee, 1966- ; Continuation Education Seminar, Western Council on
Higher Education for Nurses, 1959-64; Graduate Seminar, Western Council
on Higher Education for Nurses, 1966- ; Membership and Curriculum
Committee of Colorado League for Nursing; prior to 1954; Advisory
Committee, Los Angeles City College Program in Nursing; Chairman, Ad
Hoc State Committee on Jr. College Nurse Teacher Credential, California
League for Nursing and California Nurses Association; Selective Service
System Hawaiian Advisory Committee; Home Health Services Committee,
Hawaii State Department of Health; State Advisory Committee to the "Education,
Research, Training and Demonstration, in the Fields of Heart Disease, Cancer,
Stroke and Related Diseases Program; Liaison Task Force, Hospital Support
Positions; Advisory Committee to the Straub Medical Research Institute Pro-
ject on the Periodic Examination of the Apparently Well Individual; Nursing
Needs Subcommittee on Hawaii Nurses Association and Hawaii League for
Nursing; Patient Care Committee, St. Frances Hospital; Advisory Board for
Acute Cardiac (Coronary) Training Proposal, St. Francis Hospital; PHI
KAPPA PHI, University of Hawaii Chapter.
Business and Professional Affiliations: Visiting Assistant Professor, University
of California School of Nursing; Lecturer in Nursing, University of Calif. School
of Nursing; Lecturer and Assoc. Research Nurse; Director of Pre-Service
Program for the Preparation of Nurse Faculty for Associate Degree Programs
in Nursing, Univ. of Calif. School of Nursing; Associate Professor, Univ.
of Calif. School of Nursing; Short Term Consultant, World Health Organization,
Chile, June - August 1964 & 65.

Dr. Dunlap also serves on several University Committees at the University
of Hawaii. Consultation and Community Services include: Member of State
Board of Nurse Examiners in Colorado for five years; served as President
for 1 year; Speaker and Program Director, two-day Conference on Development

5

## Page 86

<u>Dr. Marjorie Dunlap (continued)</u>

of Communication skills for Veterans Administration Hospital, Whipple, Arizona; Consultant, St. Vincent's Hospital School of Nursing; Project Chairman and Coordinator, WICHE, Step I, Central Training Course, Short-Term Training Program for Nurses in Leadership Positions; Consultant and Trainer, Annual Institute conducted by California State Board of Nurse Examiners, "The Interviewing Process"; Consultant to Step II, WICHE, Continuation Education Program, UCLA; Conference Corrdinator, Three Summer Workshops on Teaching of Clinical Nursing in Associated Degree Programs in Nursing; Conference Coordinator, Workshop on Associate Degree Programs in Nursing, UCLA; Consultant to San Jose Associate Degree Nursing Program; Moderator, Panel on Intensive Care Units, American College of Surgeons; Consultant, Los Angeles County Hospital School of Nursing; Consultant to University of Nevada School of Nursing; Resource Staff and Group Leader, CNA Intersectional Workshop; Conducted two and one-half day workshop for Navy Nurses, U. S. Naval Hospital, San Diego; Consultant to Queen's Hospital School of Nursing, Hawaii; Consultant to Naha School of Nursing and Koza Hospital School of Nursing, Okinawa.
<u>Public Lectures and Forums:</u> "Issues and Problems in Nursing and Nursing Education", CNA Intersectional Workshop, Asilomar, Calif. March 12, 1964; Many other lectures on Nursing were given during 1966-67.

<u>Publications, Research and Reports:</u> "The Use of Quasi-Q-Sort Methodology in Evaluating Self Perceived Conference Leadership Skill Attainment, by Dr. Dunlap, and Betty Jo Hadley - <u>Nursing Research</u>, Vol. 14, No. 2, Spring 1965.

<u>Pain and Its Alleviation, A Report on the Evaluation</u>, UCLA School of Nursing, Los Angeles, Calif. 87 pp., November 1962.
Dr. Dunlap is a member of various other organizations too numerous to mention.

Dr. Dunlap is presently Dean, School of Nursing, University of California Medical Center.

<u>Miss Beatrice Finkelstein, 1517 Nichols Street, Manhattan, Kansas 66502</u>

Native of New York City, N. Y. Graduated Hunter College (B. A.); Columbia University (M. Sc.); and has taken short courses at Iowa State University; Mass. Institute of Technology; Robert Taft Sanitary Engineering Center.
Member: Secretary-Treasurer, American Dietetic Association; President, Alabama Dietetic Associations Institute of Food Technologists; Honorary member, American Home Economics Association; Secretary-Treasurer (local branches), American Association of University Women; Audubon Society; American Public Health Association, (Fellow); Honorary Member, Phi Upsilon Omicoron; Sigma Xi.

6

## Page 87

**Miss Beatrice Finkelstein (continued)**

Business and Professional Affiliations: Research Nutritionist - Aeorspace Medical Laboratories, Wright Patterson AFB: Associate Professor, University of Utah; Consultant in Foods and Nutrition, National Aeronautics and Space Agency; Member, Food and Nutrition Sections, National Security and Industrial Association; Secretary, County Chapter, American Cancer Society; Secretary-Treasurer, Ohio State Chapter, Institute of Food Technologists; Chairman, Recruitment Section, Utah Home Economics Association.

Miss Finkelstein is a Professor, College of Home Economics, Kansas State University.

**Mrs. Sarah M. Fitzgerald, 122 North Union Street, Burlington, Vermont 05401**

Native of Burlington, Vermont. Attended Bishop DeGoesbriand Hospital School of Nursing (Diploma); University of Vermont.

Member: Board of Corporators, Camp Tara Inc.; Boston Irish Social Club; Civil Defense Organization of Vermont.

Business and Professional Affiliations: American Nurses Association; Vermont State Nurses Association; Vermont State Employees Association; President, Vermont Council of Catholic Nurses; President, DeGoesbriand, Jeanne Mance Alumni Association; Vermont Vocational Association.

Mrs. Fitzgerald is Assistant Director and Nursing Instructor, Fanny Allen Memorial School of Practical Nursing.

**Miss Harriet E. Miller, Post Office Box 1019, Helena, Montana 59601**

Native of Council, Idaho. Graduate of Whitman College (B. A.); University of Pennsylvania (M. A.); Graduate work at the University of Montana.

Member: Board of Trustees, International Journal for the Education of the Blind; National Advisory Council on Education for Health Professions in the Public Health Service; Educational Policies Commission of the National Education Association and the American Association of School Administrators; Montana Regional Medical Program Advisory Committee; Business and Professional Women; American Association of University Women; Montana Education Association; National Education Association; Life Member, Montana Congress of Parents and Teachers; Honorary Life Member, Montana Association, Future Homemakers of America; Phi Beta Kappa; Phi Kappa Phi; Psi Chi.

Business and Professional Affiliations: Elected, State Superintendent of Public Instruction, 1956; Associate Dean of Students, University of Montana; Research Chemist, Atlantic Refining Company; Laboratory Technician, U. S. Government, Ninth Service Command Laboratory.

Miss Miller is prominent in the field of Education.

7

## Page 88

<u>Mrs. Mary E. Montgomery, 424 Eisenhower Drive, Junction City, Kansas 66441</u>

Native of Junction City, Kansas. Graduated University of Kansas (A. B.);
Columbia University, School of Journalism.
Member: Miami, Florida Junior League; Kappa Alpha Theta; Kansas Press
Women; National Federation of Press Women.
Business and Professional Affiliations: Public Relations, Red Cross County
Chapter Board; Hospital Advisory Board.

Awards: Three State Awards from the Kansas Press Women and two
National awards from the National Federation of Press Women for her
column titled ''Inciden-Tally''.
Mrs. Montgomery is a columnist for the Junction City Daily Union, Inc.

<u>Mrs. Will Etta Oates, 485 Valley Club Circle, Little Rock, Arkansas 72207</u>

Native of Arkansas City, Kansas. Graduate of University of Arkansas
(B. A.).
Member: Second and First Vice President, Arkansas Federation of
Women's Clubs; President, Woman's City Club of Little Rock; President
Public Welfare Forum of Little Rock; Executive Committee, Past
Chairman (first woman in the U. S. to serve in this capacity), Salvation
Army Advisory Board; Board Member, Pulaski County T. B. Association
Board; President and only woman Board Member, Little Rock Civic
Ballet Company; Member of Chamber of Commerce; Board Member,
Arkansas Division, American Cancer Society; Pulaski County Business
Bureau, (only woman on the Board).
Business and Professional Affiliations: Member, House of Representatives of
Arkansas Legislature; Governor's Advisory Commission on the Status of Women;
appointed to the Little Rock Citizens Traffic Commission; Vice Chairman, Arkansas
Association of Women Highway Safety Leaders. Mrs. Oates is First Vice President
of the Arkansas Federation of Women's Clubs. She is also active in Public Relations
work and Commercial Advertising.

<u>Mrs. Florence M. Pickett, 2805 S. W. Rutland Terrace, Portland, Oregon 97201</u>

Native of Warren, Oregon.
Member: Women's Advertising Club; Meptic Order of the Rose; American
Women in Radio and TV; Willamette Toastmistress; Daughters of the Nile;
Eastern Star; Portland Women's Research; Fashion Group International;
St. Vincent Hospital Guild; Oregon Press Club; Aftra and Agva; Arlington
Heights Symphony Auxiliary; Board of the Sunshine Division of the Portland
Police Bureau; Shrine Hospital Birthday Committee; Governor's Committee
on Home Safety; International Seaman's Club; Den Mother, Portland Rain-
makers; Theta Sigma Phi.
Business and Professional Affiliations: Former Assistant Dance Director,
MGM and Selznick Studios in Hollywood; Judge, Junior Rose Festival Association;

8

## Page 89

Mrs. Florence M. Pickett (continued)

Judge, Miss Portland Pageant; Featured Speaker, Matrix Table at Oregon State University; Featured Speaker, Dr. Paul Dudley White's "Hearts and Husbands"; Founder, "Konnies Club"; Advisor and training instructor, Portland Meter Maids; five times chaperoned the Lucia Queen of Lights from Portland to the Scandinavian countries; First Woman to ride in a U.S. Submarine since WWII; included in Air France's first trans-polar flight Los Angeles to Paris, 1960.
Awards: Theta Sigma Phi, "OFF BEAT FEATURE" award; 1960 TV Prevue Award, "BEST FEMALE PERSONALITY"; Portland's "Woman of the Year" in 1961.
Mrs. Pickett is a Woman's Editor for Radio/TV.

Mrs. Mamie B. Reese, 614 Whitney Avenue, Albany, Georgia 31701

Native of Macon, Georgia. Graduated Spelman College (B.S.); Drake University (M.S.); Studies at Ohio State University; University of Southern California; Simmons College and Boston University.
Member: Georgia Teachers and Education Association; National Education Association; Sigma Rho Sigma Honor Society; Auxiliary to the Southeastern Medical Society; Treasurer, Auxiliary to the Georgia Osteopathic Medical Association; National Mental Health Association; National Association of Women Deans and Counselors; Delta Sigma Theta Sorority, National Sorority; Church Women United; Board of Directors of the Flint River Girl Scout Council (34 Southwest Georgia Counties); Board of Directors, Semper Fidelis, Federated Club Albany; Board of Directors, Georgia Division, American Cancer Society; Albany State College--Community Relations Committee; Chairman, Canister Division, Dougherty County Committee, National Foundation, March of Dimes; Chairman, Ways and Means, Albany Federation of Colored Women's Clubs, Inc.; Chairman, Educational Projects, Delta Sigma Theta Sorority; Chairman, Arts and Crafts, South Georgia Conference, Christian Methodist Episcopal Church; Hines Memorial Christian Methodist Episcopal Church, Albany. Church capacities served -- Past President, General Missionary Society; faculty member, Church Leadership School, Paine College, Augusta, Georgia; and Instructor, annual Missionary Institute, Interdenominational Theological Center, Atlanta, Georgia.
Business and Professional Affiliations: High School teacher at Center High School in Waycross, Georgia, and Des Moines Technical High School in Iowa; Home Demonstrator Agent in Baker and Burke Counties, Georgia; employed for 19 years at Albany State College.
Awards: Appointment to the Governor's Commission on the Status of Women, State of Georgia, 1963; cited by her Alma Mater, Spelman College, for Distinguished Service to Humanity, 1966; selected as an Outstanding Citizen by Albany State College Community Relations Committee, 1966; The Albany State College Yearbook for 1966, The Ram, was dedicated to her; listed in Who's Who Among American Women, 1968-69.
Mrs. Reese is Associate Professor of Education and Dean of Women, Albany State College.

*Handwritten: 9*

## Page 90

**Dr. Hope S. Ross, 1101 East Broadway, Enid, Oklahoma 73701**

Native of Venore, Tennessee. Attended Tennessee Wesleyan University; Maryville College (A. B.); University of Oklahoma School of Medicine (M. D.); Crippled Children's Hospital, Oklahoma City (Internship); North Hudson Hospital (Resident in Anesthesia); Commonwealth Fellow, Harvard University.
Member: Enid Chamber of Commerce; United Nations Association; Delegate to White Conference on Education; Finance Advisory Committee, Democratic Central Committee of Oklahoma; Board Member, First Methodist Church; American Medical Association; American Association of Medical Women; Oklahoma State Medical Association; Garfield-Kingfisher County Medical Society; President's Committee on Employment of the Handicapped; Governor's Advisory Committee, Statewide Planning for Vocational Rehabilitation; Board of Oklahmoa Rehabilitation Association; Southwestern Cooperative Educational Laboratory, Inc.; Board of Directors, St. Mary's Hospital School of Nursing; Garfield County Health Board; Liaison Committee, Oklahoma Academy of General Practice and University of Oklahoma School of Medicine; Planning Committee, Oklahmoa Regional Medical Programs.
Business and Professional Affiliations: American Academy of General Practice; Oklahoma Academy of General Practice; Staff Memberships at Enid General Hospital and St. Mary's Hospital; Medical Consultant on Medicare Advisory Council Committee on Physician's Participation; Area Consultant for Vocational Rehabilitation.
Dr. Ross is a self-employed Medical Doctor.

**Mrs. Eleanor P. Sheppard, 1601 Princeton Road, Richmond, Virginia 23227**

Native of Pelham, Georgia. Attended Limestone College.
Member: Business and Professional Women's Club; Soroptimist; Ginter Park Woman's Club; Richmond Area Democratic Woman's Club; Past President, Richmond Federation of PTAs; National Committee on Uniform Traffic Code; Richmond International Council Board; Virginia Wildlife Exhibit Board; Central Virginia Educational Television Board; Member, Steering Committee, Richmond Area Community Council Recreation Task Force; Chairman, Advisory Committee on Practical Nurse Education; Trustee Richmond Forward; Advisory Board for Business and Community Development, University of Virginia; Advisory Board, Camp Ruther Glen; Judge 1966-68 Sears Foundation - General Federation of Women's Clubs Community Improvement Award (April 1968); Honorary Member, Richmond Symphony Directors; National Municipal League; Virginia Municipal League; Virginia Citizens Planning Association; Kappa Delta Epsilon; Treble Clef and Book Lovers Club.
Business and Professional Affiliations: Member, Richmond City Council; Council Representative, Richmond Regional Planning and Economic Development Commission; Richmond City Planning Commission; Council

10

## Page 91

<u>Mrs. Eleanor P. Sheppard (continued).</u>

Agencies and Legislative Committee; Mayor, City of Richmond,
Virginia.
<u>Awards:</u> Richmond First Club Good Government Award; Richmond Jaycees
Gold Feather Award for Community Service.
Mrs. Sheppard is a Member, House of Delegates, Virginia General Assembly.

<u>Miss June Strelecki, 2 Berkeley Terrace 17B, Irvington, New Jersey 07111</u>

Native of New Jersey. Graduated from Drew University (B. A. ); American
University (graduate study); Harvard University (LLB).
<u>Member:</u> Past President, Business and Professional Women of Irvington,
President, Region I and National member, Executive Committee and Legal
Affairs Committee, American Association of Motor Vehicle Directors;
American Bar Association; Harvard Law School Association; Essex County
Bar Association; International Association of Chiefs of Police; President
Eastern Region Military-Civilian Traffic Safety Conference.
<u>Business and Professional Affiliations:</u> Deputy Attorney General, State
of New Jersey; Assistant Counsel to the Governor, State of New Jersey;
Assistant Prosecutor, County of Essex; Director, Indigent Depender
Program, County of Essex. Associate Partner in the law firm of Citrino,
Carella, Balsam and Crochelt.
Miss Strelecki is a Lawyer - Private Practice.

<br>
<p align="center">11</p>

## Page 92

CHARLES S. WILSON MEMORIAL HOSPITAL
33-57 HARRISON STREET
JOHNSON CITY, N. Y. 13790

*Handwritten: Opened by Marcia*

*Stamp: "JOHNSON CITY N.Y. APR 21 '70"*
*Stamp: "U.S. POSTAGE .06"*

Major General George V. Williams
Commanding Officer, U.S. Air Force
Hancock Field
Syracuse, New York 13225

## Page 93

**CHARLES S. WILSON MEMORIAL HOSPITAL**
**33-57 HARRISON STREET**
**JOHNSON CITY, N. Y. 13790**

*Handwritten: File 5-INF-2 DB*
*Handwritten: [initials]*

**M. C. STITH**
**ADMINISTRATOR**

April 21, 1970

Major General George V. Williams
Commanding Officer, U.S. Air Force
Hancock Field
Syracuse, New York

Dear General Williams:

We have now written a follow-up letter to the crew of our Mercy Flight of April 1, 1970, advising them of the success of Jerry Terela's transplant. Thank you for your letter informing us of their names and addresses.

My wife and I shall visit TSgt Pratschler's children in Matamoras within the next two weeks with a new Spring wardrobe for each. This is not charity, for which I have little use, but an investment in a man who is fulfilling his commitment to his nation and his family in spite of hardship. As I told you on the telephone, he related to me the loss of his wife last year by renal failure, so he had a real personal interest in the flight. We trust you will express yourself should you feel this is improper.

I sincerely hope to meet you personally someday very soon.

Sincerely yours,

*Handwritten: Horace Dumont*
Horace T. Dumont
Director of Public Relations

HTD: jm

*Handwritten: [Large initials/mark on right side]*

*Handwritten: I.O.*
*Handwritten: For your info - possibility of a story - however be sure not to embarrass Sgt Pratschler.*
*Handwritten: [initials]*

## Page 94

```

In []:
```python
import os
from PIL import Image
import pytesseract
import pandas as pd
import io

# Load the image to inspect it
img_path = '/mnt/data/image.png'
img = Image.open(img_path)

# Use pytesseract to extract text and layout information
# We'll use the 'data' output to get bounding boxes and confidence scores
ocr_data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DATAFRAME)

# Filter out rows with no text
ocr_data = ocr_data[ocr_data.text.notnull() & (ocr_data.text.str.strip() != "")]

# Display the first few rows of the OCR data to understand the structure
print(ocr_data.head(20))

# Display the image to manually verify the layout
img.show()

```

Out []:
```output
<output truncated>
```

In []:
```python
# Based on the visual inspection and OCR data, I will manually construct the Markdown.
# The document has a header, a right-side box/table, a main body with text, and a footer with a table.

markdown_content = """
## UNCLASSIFIED

**COORDINATION AND RECORD COPY**

| FILE CODE |
| :--- |
| 5-INF-2 *Handwritten: DB* |

| WRITE LAST NAME AND SHOW DATE COORDINATED |
| :--- |
| *Handwritten: Mar. 27 '70* |
| *Handwritten: FCM.* |
| *Handwritten: DB* |
| |
| |
| |
| |
| |
| |
| |
| |
| |
| |

UNCLAS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;X

ROUTINE

ROUTINE

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;21CIO

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HQ NORAD(NNPA)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ENT AFB., COLO.

## Page 95

*Handwritten: File 5-UNF-2 DB*

Form 90-Adm.

State of New York
Department of Mental Hygiene

*Image: Seal of the State of New York*

**SYRACUSE STATE SCHOOL**
(DATE OF OPENING—OCTOBER 1851)
**P.O. Box 1035**
**Syracuse, N. Y. 13201**
March 6, 1970

| | | |
| :--- | :---: | ---: |
| GEORGE J. BUCHHOLTZ, M.D.<br>DIRECTOR | | MAIN GROUNDS—800 S. WILBUR AVE.<br>PHONE (AREA 315) 475-5141 |
| LLOYD E. WATTS, M.D.<br>ASSISTANT DIRECTOR | | |
| PERCY V. CAMPFIELD<br>BUSINESS OFFICER | | |

Air Force Base
Office of Information
Hancock Field
Syracuse, New York

Gentlemen:

On behalf of the residents and employees, I would like to thank you sincerely for the wonderful parachute you so generously donated to the school.

The Recreation and Volunteer Departments are using the parachute in play therapy for the residents. The children enjoy their new "toy" very much, and many creative type of games and activities are being developed through the use of the parachute.

We feel that this piece of apparatus will further develop a child's finger and hand coordination when he grasps hold of it with his fellow students and raises and lowers the billowing parachute through the air. It is also a great exercisor for their arm, shoulder, abdominal and back muscles. It has many infinite uses, and will be one of the most interesting and important pieces of equipment we have for the residents.

We appreciate your interest in, and support of, the mentally retarded, and hope it will continue in the future.

Very truly yours,

*Handwritten: George Buchholtz*

George J. Buchholtz, M. D.
Director

KMC/bh

*Handwritten: Good Show. Maj M*

TELEPHONE INQUIRIES—PHYSICIANS WILL BE AVAILABLE BETWEEN 9 A.M. AND 10 A.M. MONDAY THROUGH FRIDAY
VISITING DAYS ARE ONLY ON WEDNESDAYS, SATURDAYS, SUNDAYS AND LEGAL HOLIDAYS FROM 10 A.M. TO 4 P.M.
