import requests
import os
import time
import webbrowser

R = "\033[1;91m"
G = "\033[1;92m"
Y = "\033[1;93m"
C = "\033[1;96m"
X = "\033[0m"

logo = f"""
{C}•▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬•{X}

░██████╗███╗░░░███╗░█████╗░██████╗░██╗░░██╗
██╔════╝████╗░████║██╔══██╗██╔══██╗██║░██╔╝
╚█████╗░██╔████╔██║███████║██████╔╝█████═╝░
░╚═══██╗██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗░
██████╔╝██║░╚═╝░██║██║░░██║██║░░██║██║░╚██╗
╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝

{G}𝗕𝗬: {Y}@SMARK001
{G}𝗠𝗬 𝗡𝗔𝗠𝗘: SMARK
{G}𝗧𝗛𝗘 𝗖𝗛𝗔𝗡𝗡𝗘𝗟: {Y}@pHeadersq
{G}𝗧𝗛𝗘 𝗧𝗢𝗢𝗟 𝗡𝗔𝗠𝗘: {G}INSTAGRAM INFO TOOL
{G}𝗧𝗛𝗘 𝗧𝗢𝗢𝗟 𝗕𝗜𝗢: اداة معلومات انستا
{G}𝗩𝗘𝗥𝗦𝗜𝗢𝗡: {C}v1.0
{G}𝗗𝗔𝗧𝗘: 8/10/2025
{G}𝗖𝗢𝗡𝗧𝗔𝗖𝗧: {Y}@SMARK001

{C}•▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬•{X}
"""


webbrowser.open("https://t.me/pHeadersq")


for ch in logo:
    print(ch, end='', flush=True)
    time.sleep(0.003)

SMARK = input(f"\n{Y}[+] USER: {G}")

url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={SMARK}"

headers = {
    "authority": "www.instagram.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "referer": f"https://www.instagram.com/{SMARK}/",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "x-ig-app-id": "936619743392459",
}

rs = requests.get(url, headers=headers)

if rs.status_code == 200:
    data = rs.json()
    user = data["data"]["user"]

    print(f"\n{C}📊 Instagram Profile Info\n")
    print(f"{Y}🆔 ID: {G}{user['id']}")
    print(f"{Y}👤 Name: {G}{user['full_name']}")
    print(f"{Y}🔰 Username: {G}@{user['username']}")
    print(f"{Y}✅ Verified: {G}{user['is_verified']}")
    print(f"{Y}🔒 Private: {G}{user['is_private']}")
    print(f"{Y}🧾 Bio: {G}{user['biography']}")
    print(f"{Y}👥 Followers: {G}{user['edge_followed_by']['count']}")
    print(f"{Y}👤 Following: {G}{user['edge_follow']['count']}")
    print(f"{Y}📸 Posts: {G}{user['edge_owner_to_timeline_media']['count']}")
    print(f"{Y}🖼️ Profile Picture: {G}{user['profile_pic_url_hd']}")
else:
    print(f"{R}EROR({rs.status_code})")