# -*- coding: utf-8 -*-
"""Build c09 fix/polish outputs for target lines 2403-2702."""
import io, sys

TARGET = "/Users/apple/Downloads/AI行业创业方向与生态建设讨论_原文.md"
START, END = 2403, 2702  # inclusive

with io.open(TARGET, encoding="utf-8") as f:
    lines = f.read().split("\n")

# lines[] is 0-based; target line N is lines[N-1]
blocks = []  # (header, body)
i = START - 1
while i < END:
    header = lines[i]
    body = lines[i + 1]
    blocks.append((header, body))
    i += 3

assert len(blocks) == 100, len(blocks)

# Data: target block index -> (fix_body, [polish_paragraphs])
# Removed indices (merged into a neighbor): 35, 36, 51, 55, 98
D = {}

D[0] = ("even with the the chemicals.",
        ["even with the chemicals.",
         "译：就算用了药，也没几个人破纪录。"])
D[1] = ("Yeah, yeah. And then I think one guy did.",
        ["Yeah. And then I think one guy did.",
         "译：对，然后我觉得有一个人真破了纪录。"])
D[2] = ("break a world record and he.",
        ["break a world record and he.",
         "译：破了个世界纪录，而且他……"])
D[3] = ("didn't even take anything else.",
        ["didn't even take anything else.",
         "译：而且他什么都没用。"])
D[4] = ("Are you seeing, are you seeing a pretty big increase in applications and people wanting to.",
        ["Are you seeing a pretty big increase in applications and people wanting to.",
         "译：你们看到申请和想加入的人有明显变多吗？"])
D[5] = ("Join the Spark Lab? Actually we just see, like, software applications, uh, and some hardware combines software, um, but actually we don't see very big, like a ten-million-dollar company, we don't see so much opportunities.",
        ["Join the Spark Lab? Actually we just see software applications and some hardware combines software, but we don't see very big, like a ten-million-dollar company. We don't see so much opportunities.",
         "译：加入 Spark Lab 吗？其实我们看到的多是软件应用，还有一些软硬结合的，但真没看到特别大的，比如一千万美元级别的公司，这种机会不多。"])
D[6] = ("Okay. Well, I'm saying though, since you guys have started this house, like, are there a lot more applications? Or maybe is it sort of hard?",
        ["Okay. Well, I'm saying though, since you guys have started this house, are there a lot more applications? Or maybe is it sort of hard?",
         "译：好。我是说，你们搞了这个 house（据点）之后，申请的人是不是多了很多？还是说其实挺难的？"])
D[7] = ("I was trying to like, oh.",
        ["I was trying to like, oh.",
         "译：我本来想说，哦……"])
D[8] = ("I mean, I mean.",
        ["I mean.",
         "译：我是说。"])
D[9] = ("I mean, I mean, I think of the program, ah, yeah, sure, uh, like every season we have like hundreds of founders apply, applies our program. Cool, yeah, yeah. Uh, I think the most important thing is like, uh, we need to invite more founders. We need to find them and invite them to come to the residence.",
        ["I think of the program. Yeah, sure. Like every season we have like hundreds of founders apply to our program. Cool. But I think the most important thing is we need to invite more founders. We need to find them and invite them to come to the residence.",
         "译：我是说这个项目，对，每个季度都有几百个创始人来申请。但我觉得最重要的是要主动去找更多创始人，找到他们，邀请他们来驻留。"])
D[10] = ("Yeah, you have, yeah, you have an adverse selection where it's like the same thing with resumes at a company, and then you only take the resumes that come to you, yeah.",
        ["Yeah, you have an adverse selection, like the same thing with resumes at a company. You only take the resumes that come to you.",
         "译：对，你们有逆向选择的问题，就跟公司收简历一样，你只能收到主动投来的简历。"])
D[11] = ("You have a bad date. Yeah, sure. If you go find.",
        ["You have a bad date. Yeah, sure. If you go find.",
         "译：那你们就是被动的。对，如果你们主动去找……"])
D[12] = ("the people and convince them to join, then you have much better team.",
        ["the people and convince them to join, then you have much better team.",
         "译：找到人并说服他们加入，团队就会好很多。"])
D[13] = ("Yeah, we need to, uh, go out and find them and invite them to the residence.",
        ["Yeah, we need to go out and find them and invite them to the residence.",
         "译：对，我们得走出去找到他们，邀请他们来驻留。"])
D[14] = ("Are mostly people coming from a job, or do you also take people from university?",
        ["Are mostly people coming from a job, or do you also take people from university?",
         "译：大部分人是从公司来的，还是你们也收大学生？"])
D[15] = ("Uh, you mean job, like from a comp?",
        ["Uh, you mean job, like from a comp?",
         "译：你是说工作过的，从公司来的那种？"])
D[16] = ("Like, uh, from a comp. Are most people, their previous thing was a company, or the previous thing was school?",
        ["Like, uh, from a comp. Are most people, their previous thing was a company or the previous thing was school?",
         "译：就是从公司来的。大部分人之前是在公司，还是在读书？"])
D[17] = ("Like, um, most founders, they are actually, they are, uh, young, global repeated founders, so they, they like, although they are young, like they are 25 or 20s, 26, yeah, they actually start their first start like five years ago or six years ago. So, uh, maybe as a co-founder or as a founding member, but they, uh, start several companies, start this time, like, uh, he has very experience, yeah, and like a still young, uh, repeated founder.",
        ["Like most founders, they're actually young, global repeated founders. Although they're young, like 25 or 20s, 26, they actually started their first start like five or six years ago. Maybe as a co-founder or a founding member, but they started several companies and start this time. He has very experience, and still young, repeated founder.",
         "译：大部分创始人其实都是年轻的、有全球视野的连续创业者。虽然年轻，二十五六岁，但他们五六年前就开始了第一次创业，可能做过联合创始人或创始成员，做过好几家公司，现在又出来做。经验很足，而且年纪还轻，是连续创业者。"])
D[18] = ("No time to make money, maybe. Yeah.",
        ["No time to make money, maybe. Yeah.",
         "译：可能没时间赚钱。对。"])
D[19] = ("Yeah, yeah. So our founders are like age 95 to 05.",
        ["Yeah. So our founders are like age 95 to 05.",
         "译：对。所以我们创始人大约是 95 年到 05 年出生的。"])
D[20] = ("Okay, cool.",
        ["Okay, cool.",
         "译：好，行。"])
D[21] = ("Cool. Yeah, yeah, yeah. 95 is already pretty old.",
        ["Cool. Yeah. 95 is already pretty old.",
         "译：行。对，95 年生的已经算老的了。"])
D[22] = ("Pretty old. Yeah.",
        ["Pretty old. Yeah.",
         "译：挺老了。对。"])
D[23] = ("Yeah.",
        ["Yeah."])
D[24] = ("Yeah. Okay.",
        ["Yeah. Okay."])
D[25] = ("Okay, okay. Yeah, yeah, yeah, yeah, yeah, yeah. And we also like, uh, gather some teams, like we know the team, uh, they have talent in technology, but they are not the good person to be a CEO.",
        ["Okay. Yeah. And we also like to gather some teams, like we know the team, they have talent in technology, but they're not the good person to be a CEO.",
         "译：好。我们也会整合一些团队，比如我们知道某个团队技术很强，但他们不适合当 CEO。"])
D[26] = ("So we will combine the two teams together. Does it work? Uh, I think it's work.",
        ["So we will combine the two teams together. Does it work? Uh, I think it's work.",
         "译：那我们就把两个团队合在一起。这能行吗？我觉得能行。"])
D[27] = ("I think it's work. Yeah, because, uh, they just want an opportunity to, uh, do a good, great company. Okay, so, uh, they want to join other teams. You should do your, you should develop your.",
        ["I think it's work. Yeah, because they just want an opportunity to do a good, great company. Okay, so they want to join other teams. You should do your, you should develop your.",
         "译：我觉得行得通。对，因为他们只是想要一个机会做一家好公司。所以他们愿意加入别的团队。你应该做你的、发展你自己的……"])
D[28] = ("You should develop your own founder dating app.",
        ["You should develop your own founder dating app.",
         "译：你们应该开发自己的创始人约会软件。"])
D[29] = ("There's six founders at one time. What?",
        ["There's six founders at one time. What?",
         "译：一次有六个创始人。什么？"])
D[30] = ("Is your boss?",
        ["Is your boss?",
         "译：是你老板吗？"])
D[31] = ("Yeah, yeah, yeah, yeah, yeah, cool, okay.",
        ["Yeah, cool, okay."])
D[32] = ("Yeah, and maybe like.",
        ["Yeah, and maybe like.",
         "译：对，然后可能像……"])
D[33] = ("Okay, get to Claude Code and Codex session log, and you provide unemployable only come from your code example, code session. Yeah, you do the.",
        ["Okay, get to Claude Code and Codex session log, and you provide unemployable only come from your code example, code session. Yeah, you do the.",
         "译：好，把 Claude Code 和 Codex 的会话日志拿过来，你提供的都是那些找不到工作的人，只能从你的代码示例、代码会话里来。对，你就做这个。"])
D[34] = ("Founder dating app. Yeah, yeah, yeah, yeah. You need to first, like, check the products and get help.",
        ["Founder dating app. Yeah. You need to first, like, check the products and get help.",
         "译：创始人约会软件。对。你得先看看他们的产品，再找点帮助。"])
# 35 (Patrick 02:48:59) merged into 34
# 36 (叶奇意 02:49:03) merged into 37
D[37] = ("Something like that to the fingerprint? Yeah, cool.",
        ["Something like that to the fingerprint? Yeah, cool.",
         "译：类似那样，指纹？对，挺酷的。"])
D[38] = ("Cool, okay, but, uh, I just wonder, uh, there's one problem is that from 22 and this year, we cannot see, like, all the teams, they're doing world model and like AI for Science. We keep hearing.",
        ["Cool, okay, but I just wonder, there's one problem is that from 22 and this year, we cannot see like all the teams, they're doing world model and like AI for Science. We keep hearing.",
         "译：行。但我就是好奇，有个问题，从 2022 年到现在，我们看到的团队全都在做 world model（世界模型）和 AI for Science。我们一直听到的都是这些。"])
D[39] = ("Yeah, yeah, yeah, yeah. So annoying.",
        ["Yeah. So annoying.",
         "译：对，太烦了。"])
D[40] = ("And, uh, all our teams doing world model, robotics, and AI for Science. And, uh, finally, people are not.",
        ["And all our teams doing world model, robotics, and AI for Science. And finally, people are not.",
         "译：而我们所有团队都在做世界模型、机器人和 AI for Science，到最后人们都不……"])
D[41] = ("Actually, you should have a poster that says we don't accept doctors doing these three things.",
        ["Actually, you should have a poster that says we don't accept doctors doing these three things.",
         "译：其实你们应该挂个牌子，写着我们不收做这三类研究的博士。"])
D[42] = ("Research, yeah, yeah, yeah, yeah, yeah, yeah.",
        ["Research, yeah.",
         "译：研究，对。"])
D[43] = ("You need to find.",
        ["You need to find.",
         "译：你得去找……"])
D[44] = ("Somebody who.",
        ["Somebody who.",
         "译：一个人，他……"])
D[45] = ("without you telling them to have an original idea.",
        ["without you telling them to have an original idea.",
         "译：不用你告诉他们，就有原创想法。"])
D[46] = ("Has an original idea.",
        ["Has an original idea.",
         "译：有原创的想法。"])
D[47] = ("Yeah, yeah, yeah, yeah, yeah, yeah.",
        ["Yeah."])
D[48] = ("Yeah. And, uh, I find that, uh, VCs only invest in this.",
        ["Yeah. And I find that VCs only invest in this.",
         "译：对。而且我发现 VC（风投）只投这些。"])
D[49] = ("Yeah, yeah.",
        ["Yeah, yeah."])
D[50] = ("Because they are too afraid. Yeah. VCs, VCs, VCs in China, like, I think, yeah, VCs everywhere, stupid. Yeah, this is everywhere stupid. But I think in China it's uniquely concentrated, and like they cannot, they only do consensus club deals. Yeah.",
        ["Because they are too afraid. Yeah, VCs, VCs, VCs in China, like, I think, VCs everywhere, stupid. But I think in China it's uniquely concentrated, like they cannot, they only do consensus club deals. Yeah.",
         "译：因为他们太害怕了。对，中国的 VC，到处都是这样的 VC，很蠢。但我觉得中国特别集中，他们做不了别的，只做共识性的抱团交易。对。"])
# 51 (Ryan 02:50:19) merged into 52
D[52] = ("They have a very hard time taking a risk. Yeah.",
        ["They have a very hard time taking a risk. Yeah.",
         "译：他们很难承担风险。对。"])
D[53] = ("Um, you know China, you know, in China, right away, we deal with these people.",
        ["Um, you know China, you know, in China, right away, we deal with these people.",
         "译：嗯，你懂中国，你知道，在中国我们天天跟这些人打交道。"])
D[54] = ("We, we, we deal with all these people. We, we, we deal with these people all the time, but I think it's an interesting problem. But I mean.",
        ["We deal with all these people. We deal with these people all the time, but I think it's an interesting problem. But I mean.",
         "译：我们跟这些人打交道，天天都在打交道。但我觉得这是个有意思的问题。不过我是说……"])
# 55 (叶奇意 02:50:39) merged into 56
D[56] = ("I think there's a way to communicate it where you're not telling people what to do, but you're telling people to take more risks in their ideas. Like, like, you know, maybe maybe you can indirectly also showcase founders that are doing things that are not those things, and you can say this is really cool.",
        ["I think there's a way to communicate it where you're not telling people what to do, but you're telling people to take more risks in their ideas. Like, you know, maybe you can indirectly also showcase founders that are doing things that are not those things, and you can say this is really cool.",
         "译：我觉得有办法沟通，不是直接告诉别人该做什么，而是鼓励他们在想法上多冒点险。比如你可以间接地展示那些不做这些事的创始人，然后说这个真的很酷。"])
D[57] = ("Cool, yeah, right?",
        ["Cool, yeah, right?",
         "译：行，对，是吧？"])
D[58] = ("And you're saying we're not gonna let anybody else in with this idea, but we're willing to take risk on ideas. The problem, the other issue is that the fucking FAs. Yeah, founders, what to say?",
        ["And you're saying we're not gonna let anybody else in with this idea, but we're willing to take risk on ideas. The problem, the other issue is that the fucking FAs. Yeah, founders, what to say?",
         "译：然后你说，我们不会让其他任何人带着这个想法进来，但我们愿意在想法上冒险。问题是另一个问题，那些该死的 FA（财务顾问）。对，创始人，还能说什么？"])
D[59] = ("Yeah, yeah.",
        ["Yeah, yeah."])
D[60] = ("I think so. Do you do a world model?",
        ["I think so. Do you do a world model?",
         "译：我觉得是。你做世界模型吗？"])
D[61] = ("I mean.",
        ["I mean.",
         "译：我是说。"])
D[62] = ("Like, then every FA's like, do you do a world model? And then like, we're doing world model, and then the VCs, like, here's the money. So are you from Qinghai University?",
        ["Like, then every FA's like, do you do a world model? And then like, we're doing world model, and then the VCs, like, here's the money. So are you from Qinghai University?",
         "译：然后每个 FA 都会问，你做世界模型吗？然后你说我们在做世界模型，VC 就说，钱在这。所以你是青海大学的吗？"])
D[63] = ("You know, it's like, yeah, yeah, yeah. You're from Qinghai University, I guess.",
        ["You know, it's like, yeah. You're from Qinghai University, I guess.",
         "译：你知道，就是，对，我猜你是青海大学的吧。"])
D[64] = ("Yeah, you, yeah, but yeah, but the problem is, like, the people actually don't know that the FAs are giving them bad advice, because, yeah, like, yes, of course you can get money for that idea. Do you wanna be the thirtieth company working on this? Like.",
        ["Yeah, but the problem is, the people actually don't know that the FAs are giving them bad advice. Because, yeah, like, yes, of course you can get money for that idea. Do you wanna be the thirtieth company working on this? Like.",
         "译：对，但问题是，大家其实不知道 FA 给他们的建议是错的。因为，对，当然你那个想法能拿到钱，但你想当第三十家做这个的公司吗？就这样。"])
D[65] = ("Yeah, I know this is the most precious three years. I hope that, yeah, I mean, history, you are going to waste your time.",
        ["Yeah, I know this is the most precious three years. I hope that, yeah, I mean, history, you are going to waste your time.",
         "译：对，我知道这是最宝贵的三年。我希望，对，我是说，从历史上看，你会浪费你的时间。"])
D[66] = ("Yeah, yeah.",
        ["Yeah, yeah."])
D[67] = ("So, yeah, I don't know. I mean, I think there's a way to talk about it that's not like giving people the answer, but I think you can sort of say, um.",
        ["So, yeah, I don't know. I mean, I think there's a way to talk about it that's not like giving people the answer, but I think you can sort of say, um.",
         "译：所以，对，我不知道。我是说，我觉得有办法聊这件事，不是直接给人答案，而是你可以大概说，嗯……"])
D[68] = ("Maybe you can.",
        ["Maybe you can.",
         "译：也许你可以……"])
D[69] = ("Create a very clean rule, like, yeah, like, um, like we generally don't do the same idea twice, or something like that, or maybe it's not exactly that. But I think you can. I think the more you talk about it that way, yeah, the more people will feel confidence to pitch you on riskier ideas, right? Because I think the problem is like, I remember talking to Darius, and he's like.",
        ["Create a very clean rule, like, yeah, like we generally don't do the same idea twice, or something like that, or maybe it's not exactly that. But I think you can. I think the more you talk about it that way, the more people will feel confidence to pitch you on riskier ideas, right? Because I think the problem is like, I remember talking to Darius, and he's like.",
         "译：定一条很干净的规则，比如我们一般不做重复的想法，或者类似这种，也许不完全是这样。但我觉得你可以，你越是这样说，就越多人有信心拿更冒险的想法来找你，对吧？因为我觉得问题在于，我记得跟 Darius 聊过，他说……"])
D[70] = ("Oh, it's just a game.",
        ["Oh, it's just a game.",
         "译：哦，这就是个游戏。"])
D[71] = ("It's just a game. You just, you just, it's a game to get VC money. So you would just have to tell them what they want. That's not a good strategy.",
        ["It's just a game. You just, it's a game to get VC money. So you would just have to tell them what they want. That's not a good strategy.",
         "译：这就是个游戏，就是为了拿 VC 的钱。所以你只要告诉他们想听的话就行。那不是好策略。"])
D[72] = ("Yeah, it's not a good strategy.",
        ["Yeah, it's not a good strategy.",
         "译：对，不是好策略。"])
D[73] = ("And I'm glad they're doing something different, right? Because even even their last idea was fine. But I think, I think, if you, if you like, I think a lot of people think that way, right? That's bad. Yeah, um, so yeah, I don't know.",
        ["And I'm glad they're doing something different, right? Because even their last idea was fine. But I think, if you like, I think a lot of people think that way, right? That's bad. Yeah, so yeah, I don't know.",
         "译：而且我很高兴他们在做不一样的东西，对吧？因为他们上一个想法其实也还行。但我觉得，很多人都这么想，对吧？那很糟。对，所以，我也不知道。"])
D[74] = ("I think actually the more opinionated you are, the better you'll do as an incubator, in terms of just saying like, this is the type of like a person that we want, right? And we don't, we have very low respect for like this type of behavior, right? Doesn't matter where you come from, like if you come from Qinghua, you should be much smarter. Yeah, then copy you.",
        ["I think actually the more opinionated you are, the better you'll do as an incubator, in terms of just saying like, this is the type of person that we want, right? And we have very low respect for this type of behavior, right? Doesn't matter where you come from, like if you come from Qinghua, you should be much smarter. Yeah, then copy you.",
         "译：我觉得其实你越有主见，作为孵化器就做得越好，就是明确说，这就是我们想要的那种人，对吧？我们非常看不起这种行为，对吧？不管你来自哪里，就算你来自清华，你也应该更聪明才对。对，然后抄你。"])
D[75] = ("I like this one, right? It's a game of outliers. Yeah, I mean, copying.",
        ["I like this one, right? It's a game of outliers. Yeah, I mean, copying.",
         "译：我喜欢这个说法，对吧？这是出格者的游戏。对，我是说，抄袭……"])
D[76] = ("Yeah, yeah, yeah, yeah.",
        ["Yeah."])
D[77] = ("Yeah.",
        ["Yeah."])
D[78] = ("Yeah, yeah, right. It's the opposite of an outlier behavior.",
        ["Yeah, right. It's the opposite of an outlier behavior.",
         "译：对，对。这恰恰是出格行为的反面。"])
D[79] = ("Yeah. Actually, the venture investment in China is actually, the average return is below zero. So if in distribution, you're going to lose money in the end.",
        ["Yeah. Actually, the venture investment in China, the average return is below zero. So if in distribution, you're going to lose money in the end.",
         "译：对。其实中国的风险投资，平均回报是负的。所以如果按分布来看，你最后会亏钱。"])
D[80] = ("Yeah, yeah.",
        ["Yeah, yeah."])
D[81] = ("Probably, yeah, um, I mean, the alternative is like, it's a really good time building in China.",
        ["Probably, yeah, um, I mean, the alternative is like, it's a really good time building in China.",
         "译：大概是，对，嗯，我是说，换个角度看，现在在中国创业真是好时机。"])
D[82] = ("Right? There is so much happening.",
        ["Right? There is so much happening.",
         "译：对吧？发生了太多事。"])
D[83] = ("Yeah, um, and I think also like it takes, it's just like with fundraising.",
        ["Yeah, um, and I think also like it takes, it's just like with fundraising.",
         "译：对，嗯，而且我觉得这需要花时间，就像融资一样。"])
D[84] = ("Right, it takes effort.",
        ["Right, it takes effort.",
         "译：对，需要花力气。"])
D[85] = ("Yeah, right, it sucks. Yeah, it's like it's really hard. It's not, if you do, if it feels too easy, it means you're doing.",
        ["Yeah, right, it sucks. Yeah, it's like it's really hard. It's not, if it feels too easy, it means you're doing.",
         "译：对，对啊，很痛苦。对，就是真的很难。如果不是，如果你觉得太容易，那说明你在做……"])
D[86] = ("Something wrong, actually. Yeah, right.",
        ["Something wrong, actually. Yeah, right.",
         "译：做得不对，其实。对，对。"])
D[87] = ("Um, it means you haven't pushed yourself to a place where you're doing so that you're actually taking a risk, right? So, and most people, they're trying to cash in on Qinghua. They're like, I did my work at Qinghua.",
        ["Um, it means you haven't pushed yourself to a place where you're doing so that you're actually taking a risk, right? So most people, they're trying to cash in on Qinghua. They're like, I did my work at Qinghua.",
         "译：嗯，这说明你没有把自己推到真正在冒险的位置，对吧？然后大多数人都在蹭清华的名气。他们觉得，我在清华干过活。"])
D[88] = ("Now is the time to make money, you know. And like, they realize they don't realize that, oh well, now is the time they may get hurt even more, right? They don't think about it that way, right? And all my other friends have these great jobs and do this thing where that's the opposite of a risk taker, right? So I don't know. I think the more you can communicate that to the broader community of like, you need to think differently, because we just have really low respect, and then really celebrate people who have taken a lot of risk. Like if you create that story over and over again, you're gonna attract better and better people, I think, um, because the good people will actually recognize that you, yeah, you see that opportunity.",
        ["Now is the time to make money, you know. And like, they realize they don't realize that, oh well, now is the time they may get hurt even more, right? They don't think about it that way, right? And all my other friends have these great jobs and do this thing where that's the opposite of a risk taker, right? So I don't know. I think the more you can communicate that to the broader community of like, you need to think differently, because we just have really low respect, and then really celebrate people who have taken a lot of risk. Like if you create that story over and over again, you're gonna attract better and better people, I think, because the good people will actually recognize that you see that opportunity.",
         "译：现在是赚钱的时候了，你知道吗。但他们没意识到，哦，现在可能伤得更深，对吧？他们不会这么想，对吧？而且我其他朋友都有很好的工作，做那种事，那恰恰是冒险者的反面，对吧？所以我不知道。我觉得你越能把这件事传达给更大的圈子——你需要换一种思路，因为我们真的非常鄙视（这种跟风行为），然后真的去庆祝那些冒了大险的人。如果你一遍又一遍讲这个故事，你会吸引越来越好的人，因为真正好的人会认出，你看到了那个机会。"])
D[89] = ("Yeah, yeah, to.",
        ["Yeah, yeah, to.",
         "译：对，对，去（冒险）。"])
D[90] = ("Take risk. Um, yeah. And I think, if you actually explain this to the LPs the same way, to be like.",
        ["Take risk. Um, yeah. And I think, if you actually explain this to the LPs the same way, to be like.",
         "译：去冒险。嗯，对。而且我觉得，如果你真的用同样的方式跟 LP（出资人）解释，就像说……"])
D[91] = ("I'll be like.",
        ["I'll be like.",
         "译：我就会说……"])
D[92] = ("Are you an LP in Hong Kong? Okay. Well, you already have that allocation, right? Like we can't, we're not gonna, what do you want to do? Like, just be another Hong Kong, and you want to be something different.",
        ["Are you an LP in Hong Kong? Okay. Well, you already have that allocation, right? Like we can't, we're not gonna, what do you want to do? Like, just be another Hong Kong, and you want to be something different.",
         "译：你是香港的 LP 吗？好。那你已经有那个配置了，对吧？我们没法，我们不会，你想做什么？就是，别再做一个香港了，你想做点不一样的。"])
D[93] = ("Like investment returns should.",
        ["Like investment returns should.",
         "译：就像投资收益应该……"])
D[94] = ("be diversified. Yeah, yeah, yeah, yeah.",
        ["be diversified. Yeah.",
         "译：分散化。对。"])
D[95] = ("Yeah, so yeah, cool.",
        ["Yeah, so yeah, cool.",
         "译：对，所以，行。"])
D[96] = ("Yeah. I think our position is totally different from with other ventures. Yeah, yeah.",
        ["Yeah. I think our position is totally different from with other ventures. Yeah.",
         "译：对。我觉得我们的定位跟其他风投完全不一样。对。"])
D[97] = ("It's taking a long time to build it. But like, it's gonna work. You shouldn't, shouldn't be scared of. You should be leaning into it.",
        ["It's taking a long time to build it. But like, it's gonna work. You shouldn't be scared of. You should be leaning into it.",
         "译：建这个东西要花很长时间。但它会成的。你不该害怕。你应该投入进去。"])
# 98 (Ryan 02:55:36) merged into 99
D[99] = ("The more you become an outlier, the more people wanna back you if you're right.",
        ["The more you become an outlier, the more people wanna back you if you're right.",
         "译：你越成为出格者，如果你是对的，就越多人愿意支持你。"])

KEPT = sorted(D.keys())
assert KEPT == [i for i in range(100) if i not in (35, 36, 51, 55, 98)], KEPT

def block_text(header, body):
    return header + "\n" + body

fix_blocks = []
pol_blocks = []
for idx in KEPT:
    header, _ = blocks[idx]
    fix_body, pol_paras = D[idx]
    fix_blocks.append(block_text(header, fix_body))
    pol_blocks.append(block_text(header, "\n\n".join(pol_paras)))

fix_out = "\n\n".join(fix_blocks) + "\n"
pol_out = "\n\n".join(pol_blocks) + "\n"

with io.open("/Users/apple/Documents/deepseek/Working-Place/out/fix/c09.md", "w", encoding="utf-8") as f:
    f.write(fix_out)
with io.open("/Users/apple/Documents/deepseek/Working-Place/out/polish/c09.md", "w", encoding="utf-8") as f:
    f.write(pol_out)

print("fix blocks:", len(fix_blocks), "polish blocks:", len(pol_blocks))
print("fix lines:", fix_out.count("\n"), "polish lines:", pol_out.count("\n"))
