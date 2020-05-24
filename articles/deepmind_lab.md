deepmind/lab

# DMLab-30

DMLab-30 is a set of environments designed for DeepMind Lab. These environments enable a researcher to develop agents for a large spectrum of interesting tasks either individually or in a multi-task setting. We have released 28 levels. Two remaining levels will be added soon.

## Rooms

### Collect Good Objects

 [ ![Human player test](../_resources/6a96bd8ce6c3d3cab4f6968f16daf41b.jpg)](https://www.youtube.com/watch?v=k0mk0CI7G0s)  [ ![Performance of IMPALA architecture](../_resources/66f39c1523e07a1212921e35e75bb4b7.jpg)](https://www.youtube.com/watch?v=3F8RJ7G3cPg)

The agent must learn to collect good objects and avoid bad objects in two environments. During training, only some combinations of objects/environments are shown, hence the agent could assume the environment matters to the task due to this correlational structure. However it does not and will be detrimental in a transfer setting. We explicitly verify that by testing transfer performance on a held-out objects/environment combination. For more details, please see:[Higgins, Irina et al. "DARLA: Improving Zero-Shot Transfer in Reinforcement Learning" (2017)](https://arxiv.org/abs/1707.08475).

Test Regime: Test set consists of held-out combinations of objects/environments never seen during training.

Observation Spec: RGBD
Level Name: `rooms_collect_good_objects_{test,train}`

### Exploit Deferred Effects

 [ ![Human player test](../_resources/ae539b7907cebefdb657f275b2dc4aed.jpg)](https://www.youtube.com/watch?v=HIkWgTAn7Rs)  [ ![Performance of IMPALA architecture](../_resources/e676d2cf6605e0e45723964cf28e1933.jpg)](https://www.youtube.com/watch?v=--BSrVGahGk)

This task requires the agent to make a conceptual leap from picking up a special object to getting access to more rewards later on, even though this is never shown in a single environment and is costly. Expected to be hard for model-free agents to learn, but should be simple when using some model-based/predictive strategy.

Test Regime: Tested in a room configuration never seen during training, where picking up a special object suddenly becomes useful.

Observation Spec: RGBD
Level Name: `rooms_exploit_deferred_effects_{test,train}`

### Select Non-matching Object

 [ ![Human player test](../_resources/6464cd54ff6747fbac92745d9fccc62b.jpg)](https://www.youtube.com/watch?v=mMD12_7gYGc)  [ ![Performance of IMPALA architecture](../_resources/2c873232bee3a0e720736c4a2c6a172f.jpg)](https://www.youtube.com/watch?v=46hxLxkrLlk)

This task requires the agent to choose and collect an object that is different from the one it is shown. The agent is placed into a small room containing an out-of-reach object and a teleport pad. Touching the pad awards the agent with 1 point, and teleports them to a second room. The second room contains two objects, one of which matches the object in the previous room.

- Collect matching object: -10 points.
- Collect non-matching object: +10 points.

Once either object is collected the agent is returned to the first room, with the same initial object being shown.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `rooms_select_nonmatching_object`

### Watermaze

 [ ![Human player test](:/be804fa880fc52bba0e1cd03f9b5a672)](https://www.youtube.com/watch?v=XaI6SjFcmd0)  [ ![Performance of IMPALA architecture](../_resources/35c4eb20494679144e304d986c180693.jpg)](https://www.youtube.com/watch?v=9XkGLVvY4yg)

The agent must find a hidden platform which, when found, generates a reward. This is difficult to find the first time, but in subsequent trials the agent should try to remember where it is and go straight back to this place. Tests episodic memory and navigation ability.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `rooms_watermaze`

### Keys Doors Puzzle

 [ ![Human player test](:/d6d68c2c2e936e92fd9afeeb85dcb161)](https://www.youtube.com/watch?v=FYTeAUUiwpQ)  [ ![Performance of IMPALA architecture](../_resources/e1838c47f5035724081928f57cf04b43.jpg)](https://www.youtube.com/watch?v=kdM6rzP557s)

A procedural planning puzzle. The agent must reach the goal object, located in a position that is blocked by a series of coloured doors. Single use coloured keys can be used to open matching doors and only one key can be held at a time. The objective is to figure out the correct sequence in which the keys must be collected and the rooms traversed. Visiting the rooms or collecting keys in the wrong order can make the goal unreachable.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `rooms_keys_doors_puzzle`

## Language

For details on the addition of language instructions, see:[Hermann, Karl Moritz, & Hill, Felix et al. "Grounded language learning in a simulated 3D world. (2017)"](https://arxiv.org/abs/1706.06551).

### Select Described Object

 [ ![Human player test](../_resources/2fd27d48efaf5b12ec391879e2b97b1e.jpg)](https://www.youtube.com/watch?v=JCJOgEcNgKY)  [ ![Performance of IMPALA architecture](../_resources/05f5a5dfe451f87daeb89821f89c6143.jpg)](https://www.youtube.com/watch?v=P2mp3zSHFOU)

The agent is placed into a small room containing two objects. An instruction is used to describe one of the objects. The agent must successfully follow the instruction and collect the goal object.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD and language
Level Name: `language_select_described_object`

### Select Located Object

 [ ![Human player test](../_resources/4522907ed929571bfd756533dd49659b.jpg)](https://www.youtube.com/watch?v=I_NmlAn_3gY)  [ ![Performance of IMPALA architecture](../_resources/3985aef8999dfb313b8a3df1e27751cc.jpg)](https://www.youtube.com/watch?v=Ko7f9hnX5es)

The agent is asked to collect a specified coloured object in a specified coloured room. Example instruction: “Pick the red object in the blue room.” There are four variants of the task, each of which have an equal chance of being selected. Variants have a different amount of rooms (between 2-6). Variants with more rooms have more distractors, making the task more challenging.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD and language
Level Name: `language_select_located_object`

### Execute Random Task

 [ ![Human player test](../_resources/4d6f547002c63bb339a79d700003af26.jpg)](https://www.youtube.com/watch?v=6sIQoHeYaP8)  [ ![Performance of IMPALA architecture](../_resources/230e1026bf2732f768cc94e8fc58b4d9.jpg)](https://www.youtube.com/watch?v=1sFeDd3jHHk)

The agent is given one of seven possible tasks, each with a different type of language instruction. Example instruction: “Get the red hat from the blue room.” The agent is rewarded for collecting the correct object, and penalised for collecting the wrong object. When any object is collected, the level restarts and a new task is selected.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD and language
Level Name: `language_execute_random_task`

### Answer Quantitative Question

 [ ![Human player test](../_resources/112329530c6f89ed8baf79a0ed491cef.jpg)](https://www.youtube.com/watch?v=QMtSQI_r2ag)  [ ![Performance of IMPALA architecture](../_resources/18cb76ee420110d476c334b33569d9ff.jpg)](https://www.youtube.com/watch?v=kspqM0D2nu8)

The agent is given a yes or no question based on object colors and counts. The agent selects a certain object to respond:

- White sphere = yes
- Black sphere = no
- Example questions:
- “Are all cars blue?”
- “Is any car blue?”
- “Is anything blue?”
- “Are most cars blue?”

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD and language
Level Name: `language_answer_quantitative_question`

## LaserTag

### One Opponent Small

 [ ![Human player test](:/d0acb87a8d2f393d0d25763ba8b29a6c)](https://www.youtube.com/watch?v=Sv32PoqL390)

This task requires the agent to play laser tag in a procedurally generated map containing random gadgets and power-ups. The map is small and there is 1 opponent bot of difficulty level 4. The agent begins the episode with the default Rapid Gadget and a limit of 100 tags. The agent’s Shield will begin at 125 and slowly drop to the max amount of 100. The gadgets, powerups and map layout are random per episode and so the agent must adapt to each new environment.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `lasertag_one_opponent_small`

### Three Opponents Small

 [ ![Human player test](../_resources/f813d936500a46a5d2236970e8fe5da6.jpg)](https://www.youtube.com/watch?v=yj7_5zFP8pA)

This task requires the agent to play laser tag in a procedurally generated map containing random gadgets and power-ups. The map is small and there are 3 opponent bots of difficulty level 4. The agent begins the episode with the default Rapid Gadget and a limit of 100 tags. The agent’s Shield will begin at 125 and slowly drop to the max amount of 100. The gadgets, powerups and map layout are random per episode and so the agent must adapt to each new environment.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `lasertag_three_opponents_small`

### One Opponent Large

 [ ![Human player test](../_resources/a0fb78c424574be78a8deffe7ae1b4f3.jpg)](https://www.youtube.com/watch?v=iNNL8XXj-YI)  [ ![Performance of IMPALA architecture](../_resources/cddc610245406143612206bbcf3cc0f1.jpg)](https://www.youtube.com/watch?v=H6DBUNni2Ak)

This task requires the agent to play laser tag in a procedurally generated map containing random gadgets and power-ups. The map is large and there is 1 opponent bot of difficulty level 4. The agent begins the episode with the default Rapid Gadget and a limit of 100 tags. The agent’s Shield will begin at 125 and slowly drop to the max amount of 100. The gadgets, powerups and map layout are random per episode and so the agent must adapt to each new environment.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `lasertag_one_opponent_large`

### Three Opponents Large

 [ ![Human player test](../_resources/2626591077667e98d349d73a0a6e37f2.jpg)](https://www.youtube.com/watch?v=7uDO25eyBRY)

This task requires the agent to play laser tag in a procedurally generated map containing random gadgets and power-ups. The map is large and there are 3 opponent bots of difficulty level 4. The agent begins the episode with the default Rapid Gadget and a limit of 100 tags. The agent’s Shield will begin at 125 and slowly drop to the max amount of 100. The gadgets, powerups and map layout are random per episode and so the agent must adapt to each new environment.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `lasertag_three_opponents_large`

## NatLab

### Fixed Large Map

 [ ![Human player test](../_resources/d4600177bbda7577e88424f65926f133.jpg)](https://www.youtube.com/watch?v=urYc9vaWQ7A)  [ ![Performance of IMPALA architecture](../_resources/6f39b52da87997bdfd11d05784f11baf.jpg)](https://www.youtube.com/watch?v=ucJEnnn5iC8)

This is a long term memory variation of a mushroom foraging task. The agent must collect mushrooms within a naturalistic terrain environment to maximise score. The mushrooms do not regrow. The map is a fixed large-sized environment. The time of day is randomised (day, dawn, night). Each episode the spawn location is picked randomly from a set of potential spawn locations.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `natlab_fixed_large_map`

### Varying Map Regrowth

 [ ![Human player test](../_resources/a186c5db0fe4ae1bdeed772922791729.jpg)](https://www.youtube.com/watch?v=pcIznPLhGpc)  [ ![Performance of IMPALA architecture](../_resources/10a8a78281cd6481f06169e0b86eb009.jpg)](https://www.youtube.com/watch?v=P0ctwiDvcN4)

This is a short term memory variation of a mushroom foraging task. The agent must collect mushrooms within a naturalistic terrain environment to maximise score. The mushrooms regrow after around one minute in the same location throughout the episode. The map is a randomized small-sized environment. The topographical variation, and number, position, orientation and sizes of shrubs, cacti and rocks are all randomized. The time of day is randomised (day, dawn, night). The spawn location is randomised for each episode.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `natlab_varying_map_regrowth`

### Varying Map Randomized

 [ ![Human player test](../_resources/2e1eac690a4a0db74299709de242d0cb.jpg)](https://www.youtube.com/watch?v=S58T_obXZYk)  [ ![Performance of IMPALA architecture](../_resources/db3d0b4becf8d52ef94ef88a4ee4445d.jpg)](https://www.youtube.com/watch?v=TnH5v0859U8)

This is a randomized variation of a mushroom foraging task. The agent must collect mushrooms within a naturalistic terrain environment to maximise score. The mushrooms do not regrow. The map is randomly generated and of intermediate size. The topographical variation, and number, position, orientation and sizes of shrubs, cacti and rocks are all randomised. Locations of mushrooms are randomized. The time of day is randomized (day, dawn, night). The spawn location is randomized for each episode.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `natlab_varying_map_randomized`

## SkyMaze

### Irreversible Path Hard

 [ ![Human player test](../_resources/5c418b7cf293d24791b860ca0196e285.jpg)](https://www.youtube.com/watch?v=cJLCbuHmsTw)  [ ![Performance of IMPALA architecture](../_resources/58f9c6254625086fa27838eae29c8f66.jpg)](https://www.youtube.com/watch?v=osuOo5wuR6I)

This task requires agents to reach a goal located at a distance from the agent’s starting position. The goal and target are connected by a sequence of platforms placed at different heights. Jumping is disabled, so higher platforms are unreachable and the agent won’t be able to backtrack to a higher platform. This means that the agent is required to plan their route to ensure they do not become stuck and fail the task.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `skymaze_irreversible_path_hard`

### Irreversible Path Varied

 [ ![Human player test](../_resources/c242841a294cb2f451a028bd73228b02.jpg)](https://www.youtube.com/watch?v=3onoF_i0ioA)  [ ![Performance of IMPALA architecture](../_resources/ba71c946c91b4a495f3cfcf6bb1ed765.jpg)](https://www.youtube.com/watch?v=3yPCTOy2-yg)

A variation of the Irreversible Path Hard task. This version of the task will select a map layout of random difficulty for the agent to solve. The jump action is disabled (NOOP) for this task.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `skymaze_irreversible_path_varied`

## PsychLab

For details, see:[Leibo, Joel Z. et al. "Psychlab: A Psychology Laboratory for Deep Reinforcement Learning Agents (2018)"](https://arxiv.org/abs/1801.08116).

### Sequential Comparison

 [ ![Human player test](../_resources/7b82ab5f2158c0b536234663677070bd.jpg)](https://www.youtube.com/watch?v=liS7e1EdW9w)  [ ![Performance of IMPALA architecture](../_resources/456409a47d3b3ba90399dc9b024a1242.jpg)](https://www.youtube.com/watch?v=foDX24n7rpY)

Two consecutive patterns are shown to the agent. The agent must indicate whether or not the two patterns are identical. The delay time between the study pattern and the test pattern is variable.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `psychlab_sequential_comparison`

### Visual Search

 [ ![Human player test](../_resources/575a18f9fc5415917c33485e62ebd089.jpg)](https://www.youtube.com/watch?v=G35bJr4aLSo)  [ ![Performance of IMPALA architecture](../_resources/741e48be73b09d55b677a1f817487383.jpg)](https://www.youtube.com/watch?v=eQntSh48zsE)

A collection of shapes are shown to the agent. The agent must identify whether or not a specific shape is present in the collection. Each trial consists of the agent searching for a pink ‘T’ shape. Two black squares at the bottom of the screen are used for ‘yes’ and ‘no’ responses.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `psychlab_visual_search`

## Explore

### Object Locations Small

 [ ![Human player test](../_resources/1b5cf5f5ddd0b8a709748156b0d0d3ce.jpg)](https://www.youtube.com/watch?v=P6ViELmBPbI)  [ ![Performance of IMPALA architecture](../_resources/f5efe275ea1d0a9a2f0922cdb058b814.jpg)](https://www.youtube.com/watch?v=JdfewHpTJ7Q)

This task requires agents to collect apples. Apples are placed in rooms within the maze. The agent must collect as many apples as possible before the episode ends to maximise their score. Upon collecting all of the apples, the level will reset, repeating until the episode ends. Apple locations, level layout and theme are randomized per episode. Agent spawn location is randomised per reset.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `explore_object_locations_small`

### Object Locations Large

 [ ![Human player test](../_resources/626700888923a33bd0a2dae111bf3ca0.jpg)](https://www.youtube.com/watch?v=JLRHiNe1wMo)  [ ![Performance of IMPALA architecture](../_resources/26b4ee8105bc442febf52230be23582d.jpg)](https://www.youtube.com/watch?v=bSzIDiWa2uY)

This task is the same as Object Locations Small, but with a larger map and longer episode duration. Apple locations, level layout and theme are randomised per episode. Agent spawn location is randomised per reset.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `explore_object_locations_large`

### Obstructed Goals Small

 [ ![Human player test](../_resources/6bec6c7505cb541cdbd34a3fc923c636.jpg)](https://www.youtube.com/watch?v=kGehDxLDLAU)  [ ![Performance of IMPALA architecture](../_resources/49bb3513a2e57af90f77165930c61c60.jpg)](https://www.youtube.com/watch?v=Py8kToAl87c)

This task is similar to Goal Locations Small - agents are required to find the goal as fast as possible, but now with randomly opened and closed doors. After the goal is found, the level restarts. Goal location, level layout and theme are randomized per episode. Agent spawn location is randomised per reset. Door states (open/closed) are randomly selected per reset, but a path to the goal always exists.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `explore_obstructed_goals_small`

### Obstructed Goals Large

 [ ![Human player test](../_resources/6894db812828389867aaa7c27d7e3ee7.jpg)](https://www.youtube.com/watch?v=6RtJ45V_3Ds)  [ ![Performance of IMPALA architecture](:/e2b16855d5d2040c132739173ecfe2cf)](https://www.youtube.com/watch?v=nGddvGLvkbk)

This task is the same as Obstructed Goals Small, but with a larger map and longer episode duration. Goal location, level layout and theme are randomised per episode. Agent spawn location is randomised per reset. Door states (open/closed) are randomly selected per reset, but a path to the goal always exists.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `explore_obstructed_goals_large`

### Goal Locations Small

 [ ![Human player test](../_resources/c46d33404a11cfbd3c06bf24104801ae.jpg)](https://www.youtube.com/watch?v=_tUXM7ZfvU4)  [ ![Performance of IMPALA architecture](../_resources/4e34b20cba5e9ebfec1c452495a33e3b.jpg)](https://www.youtube.com/watch?v=olSyE5pEClE)

This task requires agents to find the goal object as fast as possible. After the goal object is found, the level restarts. Goal location, level layout and theme are randomised per episode. Agent spawn location is randomised per reset.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `explore_goal_locations_small`

### Goal Locations Large

 [ ![Human player test](../_resources/b03569b91209b3b720bc17fc56e78dfb.jpg)](https://www.youtube.com/watch?v=Do-a5RreNTI)  [ ![Performance of IMPALA architecture](../_resources/62917f112dc3733b0cb980824d4d6250.jpg)](https://www.youtube.com/watch?v=nZFl9Wza8RA)

This task is the same as Goal Locations Small, but with a larger map and longer episode duration. Goal location, level layout and theme are randomised per episode. Agent spawn location is randomised per reset.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `explore_goal_locations_large`

### Object Rewards Few

 [ ![Human player test](../_resources/e59012032ae5aa585ed76e00541c8dd9.jpg)](https://www.youtube.com/watch?v=CWsEIudVNVA)  [ ![Performance of IMPALA architecture](../_resources/b12913b70cc860a8157054456ede6da0.jpg)](https://www.youtube.com/watch?v=aML4OoHUZes)

This task requires agents to collect human-recognisable objects placed around a room. Some objects are from a positive rewarding category, and some are negative. After all positive category objects are collected, the level restarts. Level theme, object categories and object reward per category are randomised per episode. Agent spawn location, object locations and number of objects per category are randomised per reset.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `explore_object_rewards_few`

### Object Rewards Many

 [ ![Human player test](../_resources/c99f59648dd9a86ce1216c35a41c6eeb.jpg)](https://www.youtube.com/watch?v=N7c-0Vg4he8)  [ ![Performance of IMPALA architecture](:/be25839a8b1a16cd894589ec4625f504)](https://www.youtube.com/watch?v=uHisk5tA8i4)

This task is a more difficult variant of Object Rewards Few, with an increased number of goal objects and longer episode duration. Level theme, object categories and object reward per category are randomised per episode. Agent spawn location, object locations and number of objects per category are randomised per reset.

Test Regime: Training and testing levels drawn from the same distribution.
Observation Spec: RGBD
Level Name: `explore_object_rewards_many`