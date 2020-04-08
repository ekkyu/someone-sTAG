# someone-sTAG
Want to get someone's Hashtag? Use this.


## fetch_plof_and_hashtag.py

When you enter someone's Instagram ID to `user_name`, the following information will be returned:

- [ ] username
- [ ] url
- [ ] icon_src
- [ ] biography
- [ ] country
- [ ] post
- [ ] follow
- [ ] follower
- [ ] hashtag : Top 30 from recent 12 tweets

For example, for `user_name="ekkkkyu"`

```
{'username': 'ekkkkyu',
 'url': 'https://www.instagram.com/ekkkkyu/',
 'icon_src': 'https://scontent-nrt1-1.cdninstagram.com/v/t51.2885-19/s150x150/84331852_666069874206915_4704859905075445760_n.jpg?_nc_ht=scontent-nrt1-1.cdninstagram.com&_nc_ohc=6X2uv0raLzIAX8cgmQW&oh=36927fcca5ff6fe835f3f2feebc62880&oe=5EB7566C',
 'biography': '5パーセントの確率でインスタ映えする写真をアップします\n🇯🇵 ✈ 🇦🇺🇨🇳🇰🇷🇹🇼🇩🇪🇫🇷🇮🇹🇻🇦🇻🇳🇵🇭🇺🇸🇸🇬🇹🇭',
 'country': 'JP',
 'post': 213,
 'follow': 715,
 'follower': 673,
 'hashtag': ('#sydneyharbourbridge',
  '#operahouse',
  '#haighschocolate',
  '#queenvictoriabuilding',
  '#kirribilli',
  '#キリビリ',
  '#bluemountains',
  '#wentworthfalls',
  '#uts',
  '#utsbusinessbuilding',
  '#sydneylunapark',
  '#lunapark',
  '#lunaparksydney',
  '#sydneyoperahouse',
  '#harbourbridge',
  '#sydneyferry',
  '#sydneyferries',
  '#mrsmacquarieschair',
  '#grilld',
  '#hamburger',
  '#burger',
  '#sydney',
  '#sydneytransport',
  '#australia',
  '#シドニー',
  '#シドニー留学',
  '#townhall',
  '#sydneytownhall',
  '#townhallsydney')}
  ```
  
## plof_img/
  
Icons are saved to this dir.

The file name when saved is `user_name.png`
