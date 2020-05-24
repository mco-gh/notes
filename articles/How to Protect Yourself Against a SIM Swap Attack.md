How to Protect Yourself Against a SIM Swap Attack

A spate of [hacked](https://mashable.com/2018/08/13/instagram-hack-locked-out-of-account) Instagram accounts. A $220 million lawsuit against AT&T. A [bustling underground crime ring](https://motherboard.vice.com/en_us/article/vbqax3/hackers-sim-swapping-steal-phone-numbers-instagram-bitcoin). They all have roots in an old problem that has lately found new urgency: [SIM card swaps](https://www.wired.com/2016/06/even-ftcs-lead-technologist-can-get-hacked/), a scam in which hackers steal your mobile identity—and [use it to upend your life](https://www.wired.com/2012/08/apple-amazon-mat-honan-hacking/).

At its most basic level, a SIM swap is when someone convinces your carrier to switch your phone number over to a SIM card they own. They’re not doing it for prank call cover, or to rack up long-distance charges. By diverting your incoming messages, scammers can easily complete the [text-based two-factor authentication](https://www.wired.com/2016/06/hey-stop-using-texts-two-factor-authentication) checks that protect your most sensitive accounts. Or, if you don’t have two-factor set up in the first place, they can use your phone number to trick services into coughing up your passwords.

> 'In most of the cases that we’ve seen, a sufficiently determined attacker can just take over someone’s online footprint.'

—Allison Nixon, Flashpoint

SIM attacks appear to be behind a recent string of Instagram takeovers, as well as the very unfortunate, not great time a hacker [posted](https://www.buzzfeed.com/christianzamora/selena-gomez-and-the-hack) Justin Bieber nudes from Selena Gomez’s account last year. But they can impact other corners of your life as well. A cryptocurrency investor this week claimed that a SIM swap resulted in the theft of $23.8 million-worth of tokens; he’s [suing](http://globenewswire.com/news-release/2018/08/15/1552594/0/en/Cryptocurrency-Entrepreneur-and-Investor-Michael-Terpin-Sues-Too-Big-to-Care-AT-T-for-Permitting-23-8-Million-Theft-in-SIM-Swap-Scam-by-Authorized-Agent.html) his carrier, AT&T, for 10 times that amount. And *Motherboard* recently documented [a number of incidents](https://motherboard.vice.com/en_us/article/j5bpg7/sim-hijacking-t-mobile-stories) in which SIM hijackers drained thousands of dollars out of people’s checking accounts.

A sobering caveat: If a skilled SIM hijacker targets you, there’s realistically not much you can do to stop them, says Allison Nixon, threat research at security firm Flashpoint. “In most of the cases that we’ve seen, a sufficiently determined attacker can take over someone’s online footprint,” she says.

That’s because ultimately, the machinations behind SIM swaps are largely out of your control. Perfect security hygiene won’t always keep someone from fooling your carrier, and in fact, they may not even have to; Flashpoint has found [some indications](https://www.flashpoint-intel.com/blog/sim-swap-fraud-account-takeover/) that SIM hijackers recruit retail workers at mobile shops to gain access to protected accounts. A comprehensive SIM swap fix would require fundamentally rethinking the role of phone numbers in 2018. “Phone numbers were never intended to be a way to confirm someone’s identity,” says Nixon. “Phone companies were never in the business to sell identity documents. It was imposed on them.”

The good news is, you can take steps to limit the chances that a SIM swap attack will happen to you—and limit the fallout if it does.

### Stick a PIN in It

Every major US carrier offers you the option of putting a PIN or a passcode on your account. Take them up on it. Having one adds another layer of protection, another piece of information an attacker needs before they can compromise your identity. That won’t help against an insider threat, but it’s much better than nothing.

On AT&T, you can set up a “wireless passcode” that’s four to eight digits long by going to your profile, then **Sign-in info**, then **Get a new passcode**. You should also add what the carrier calls “extra security,” which just means it’ll require the passcode to manage your account online or in a retail store. You can find that by going again to **Sign-in info**, then **Wireless passcode**, and checking **Manage extra security**.

Verizon actually requires a PIN, but to set yours up or change it, head to [this site](https://myaccount.verizonwireless.com/clp/login?redirect=/vzw/accountholder/profile/createBillingPassCode.action), then sign into your account. Enter the PIN of your choice twice, click **Submit**, and you’re done.

For T-Mobile, you have to call instead; dial 611 from your mobile phone and ask to add “Port Validation” to your account, which lets you choose a six to 15 digit PIN. On Sprint, sign into your account, click on **My Sprint**, then go to **Profile and security**. Scroll to **Security information**, and update your PIN there.

Yes, remembering another PIN is a pain, especially when you’ll likely only need it every couple of years. But it’s worth the effort. “Most people have that turned off because if they can’t remember their PIN they can’t go into the local Verizon store and get a new phone,” says Chet Wisniewski, principle research scientist at security firm Sophos. “If you can turn a PIN on with your mobile carrier to prevent your number from being manipulated, you should. Go ahead and write it down. No one’s going to break into your house and steal your notepad from underneath your underwear in your secret drawer in your bedroom.”

### Use Better Two-Factor

We’ve [talked about this recently](https://www.wired.com/story/two-factor-authentication-apps-authy-google-authenticator/), but it bears repeating. Getting your two-factor authentication codes over SMS is better than nothing, but it [won’t help at all](https://www.wired.com/2016/06/hey-stop-using-texts-two-factor-authentication/) if a SIM swap hits. What *will* work? Using an authentication app instead.

Apps like Google Authenticator and Authy give you that extra layer of security like SMS-based two-factor does, but they also tie it to your physical device rather than the number the phone company assigned to you. They show you a six-digit code that updates every 30 seconds or so, and stays in constant sync with whatever service you connect them to.

> 'The challenge we have is these app developers need a universal identifier, and they’ve just decided that the phone numbers as good as anything.'

—Chet Wisniewski, Sophos

Want to step your two-factor up even further? Opt instead for a physical authentication method, [like a Yubikey](https://www.wired.com/story/how-to-use-a-yubikey/). These little fobs fit on your keychain, and plug into your computer’s USB port to help verify your identity. (For what it's worth, [you can get a free YubiKey 4 with a new WIRED subscription](https://subscribe.condenastdigital.com/subscribe/splits/wired/WIR_FAILSAFE).) “If you’ve enabled a phsyical token, plus your password, and you turn off SMS, then someone literally is going to have to steal your keys. That raises the stakes to a whole other level,” says Wisniewski.

Not all services allow for tougher two-factor. (Instagram’s the most notable example, although the social network says it’s working on expanding the options it offers.) But switch it on where you can to give yourself the best shot at staying safe.

### Extra Measures

If a hacker has a phone number that’s associated with some of your online accounts, they can sometimes circumvent two-factor requirements altogether—which gets back to the problem of using phone numbers as identifiers in the first place. Disentangling yourself from those seven digits is hard to do at scale, but it’s worth at least trying on especially sensitive accounts, or if you might be a high-value target.

“If there’s one particular thing that you have that you know a thief would go after, like your bank account or your bitcoin holdings or your user name on social media, obviously keep that account separate from the rest of your online identity,” says Nixon. “If you’re extra paranoid, you can have a separate phone number, and keep that phone number secret. I know that’s kind of over the top, but some people who try to protect themselves from this attack vector do try things like that.”

For services that require a phone number of some sort on record, you can swap in a Google Voice number, for instance. But Wisniewski suggests that the added complexity it adds to your life might not be worth it for most people, especially since so many apps tie your account to the number associated with your phone. Which, again, gets back to the core problem.

“The challenge we have is these app developers need a universal identifier, and they’ve just decided that the phone numbers as good as anything. We don’t want national ID cards, and we don’t have any central authentication authority,” says Wisniewski. “They’re struggling to find something they can use to identify you, and sadly they’ve decided on the phone number, which is not incredibly secure.”

The other step you can take, however pat it sounds, is vigilance. If your smartphone suddenly stops working, or messages stop going through, you know you’ve lost your SIM. The sooner you act to preempt account takeovers from there, the better off you’ll be.

* * *

### More Great WIRED Stories

- Elon Musk has a plan to save [LA Dodger fans from traffic](https://www.wired.com/story/elon-musk-boring-company-tunnel-los-angeles-dodger-stadium/?mbid=BottomRelatedStories_Sections_2)
- Police bodycams can be hacked [to doctor footage](https://www.wired.com/story/police-body-camera-vulnerabilities/?mbid=BottomRelatedStories_Sections_2)
- Wildfire smoke kills—even [where you don't expect it](https://www.wired.com/story/wildfire-smoke-kills-where-you-dont-expect-it/?mbid=BottomRelatedStories_Sections_2)
- PHOTO ESSAY: The techies of Kenya's [Silicon Savannah](https://www.wired.com/story/kenya-silicon-savannah-photo-gallery/?mbid=BottomRelatedStories_Sections_2)
- The strange David and Goliath saga [of radio frequencies](https://www.wired.com/story/wireless-mics-radio-frequencies-fcc-saga/?mbid=BottomRelatedStories_Sections_2)
- Get even more of our inside scoops with our weekly [Backchannel newsletter](https://www.wired.com/newsletter/?name=backchannel&sourceCode=BottomStories)