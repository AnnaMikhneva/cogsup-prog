from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_f, K_g, K_h, K_j
import random
import itertools

""" Constants """
COLORS = ["red", "blue", "green", "orange"]
COLOR_KEYS = {K_f: "red", K_g: "blue", K_h: "green", K_j: "orange"}  

N_BLOCKS = 8
N_TRIALS_IN_BLOCK = 16  
TRIALS_TOTAL = N_BLOCKS * N_TRIALS_IN_BLOCK

INSTR_START = f"""
In this task, your job is to indicate the COLOR in which each word is written.

Use these keys:
F = RED
G = BLUE
H = GREEN
J = ORANGE


Press SPACE to begin.
"""

INSTR_MID = """You have finished half of the experiment, well done! Your task will be the same.\nTake a break then press SPACE to move on to the second half."""
INSTR_END = """Well done!\nPress SPACE to quit the experiment."""

FEEDBACK_CORRECT = """That was right :)"""
FEEDBACK_INCORRECT = """That was wrong :("""

""" Helper functions  """
def derangements(seq):
    perms = itertools.permutations(seq)
    return [p for p in perms if all(a != b for a, b in zip(seq, p))]

def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(*stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    return exp.clock.time - t0

def present_for(*stims, t=1000):
    dt = timed_draw(*stims)
    exp.clock.wait(max(0, t - dt))

def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, heading="Instructions")
    instructions.present()
    exp.keyboard.wait()

"""  Subject counterbalancing  """
subject_id = 1  
PERMS = derangements(COLORS)
order = (subject_id - 1) % len(PERMS)
perm = PERMS[order]

""" Experiment setup """
exp = design.Experiment(
    name="Stroop_ColorNaming",
    background_colour=C_WHITE,
    foreground_colour=C_BLACK
)
exp.add_data_variable_names(['block', 'trial', 'trial_type', 'word', 'color', 'RT', 'correct'])

control.set_develop_mode()
control.initialize(exp)

"""  Stimuli  """
fixation = stimuli.FixCross()
fixation.preload()

stims = {w: {c: stimuli.TextLine(w, text_colour=c) for c in COLORS} for w in COLORS}
load([stims[w][c] for w in COLORS for c in COLORS])

feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT)
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT)
load([feedback_correct, feedback_incorrect])

"""  Trial construction  """
base_trials = (
    [{"trial_type": "match", "word": c, "color": c} for c in COLORS] +
    [{"trial_type": "mismatch", "word": w, "color": c} for w, c in zip(COLORS, perm)]
)

trials = base_trials * (TRIALS_TOTAL // len(base_trials))
random.shuffle(trials)

""" Trial procedure  """
def run_trial(block_id, trial_id, trial):
    word = trial["word"]
    color = trial["color"]
    stim = stims[word][color]
    

    present_for(fixation, t=500)
    stim.present()
    
    key, rt = exp.keyboard.wait(COLOR_KEYS.keys())
    response_color = COLOR_KEYS.get(key, None)
    correct = (response_color == color)
    
    exp.data.add([block_id, trial_id, trial["trial_type"], word, color, rt, correct])
    
    feedback = feedback_correct if correct else feedback_incorrect
    present_for(feedback, t=700)

""" Run experiment """
control.start(subject_id=subject_id)
present_instructions(INSTR_START)

trial_counter = 0
for block_id in range(1, N_BLOCKS + 1):
    for trial_id in range(1, N_TRIALS_IN_BLOCK + 1):
        trial = trials[trial_counter]
        run_trial(block_id, trial_id, trial)
        trial_counter += 1
    if block_id == N_BLOCKS // 2:
        present_instructions(INSTR_MID)

present_instructions(INSTR_END)
control.end()

