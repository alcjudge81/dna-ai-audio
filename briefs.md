# Lesson briefs

```
HOW TO WRITE A LESSON SCRIPT (plain text, for the ear)
- Listener: Alex, chemical engineer (Princeton ChemE, MIT LGO), starting a PhD on DNA computing in the Keung lab at NC State.
  Strong: kinetics, thermodynamics, transport, ODEs, process control, statistics-style ML (random forests, boosting). New: computer science, deep learning.
- He listens while driving or doing dishes, usually at 1.25x. Nothing may depend on seeing anything.
- Length: 1,700 to 2,300 words (about 11 to 15 minutes); keystone lessons up to 3,000. Length follows the idea.
- Voices: untagged paragraphs are voice A (the narrator). A paragraph starting with [B] is voice B, used sparingly (3 to 6 short
  turns per lesson): the sharp question a chemical engineer would ask, and the self-check questions at the end. B never lectures.
- Shape: (1) a cold open of two or three sentences that poses the lesson's question; (2) 'Quick recall' of one idea from the
  previous lesson, asked then answered; (3) three or four idea blocks, each anchored to a concrete picture, ideally from chemical
  engineering; (4) 'The DNA bridge': what this means for molecular computing; (5) a recap in three sentences; (6) two or three
  self-check questions read by B, with a pause line '---' after them, and no answers (answers open the next lesson's recall).
- Numbers: say them in words when ambiguity is possible ('ten to the fifteenth', 'four and a half million'). Give each key number
  twice. Never read an equation symbol by symbol; say what it does. At most one 'equation in words' per lesson.
- Acronyms: expand on first use; avoid ones that sound bad aloud (say 'analog-to-digital converter', not ADC).
- Honesty: separate what is demonstrated from what is proposed. Give the year and lab for experimental claims. Do not invent
  figures; if a number is an estimate, say 'roughly' and give the reasoning. Facts marked CHECKED below were verified on 16 Nov 2026.
- Never mention Alex's own unpublished research ideas: the audio is hosted publicly.
- Style: plain sentences. No headings read aloud. No 'in this lesson we will'. Use '---' on its own line for a section pause.
- File format: first line '# <id> <title>'. Blank line between paragraphs. Save as scripts/<id>.txt.
- Pronunciation fixes go in engine/lexicon.tsv (regex<TAB>spoken form), not in the script.
```

## Phase 0: Orientation

### 0.1 The map (core, about 6 min)

Purpose: orient. The end state is six abilities: explain computation without silicon; put numbers on analog versus digital; follow a model from data to weights; build BINND-class models with Claude; place any molecular-computing paper on a map; judge what AI in DNA would take. Three questions to ask of any computer: what carries the signal, how is it kept clean (restoration), what limits its size. Walk the six phases in one sentence each. Explain how lessons work (recall, B's questions, self-check), Core versus Depth, lead-ins to outside items, NotebookLM prompts in the hub. Standing habit: after every item say one sentence aloud linking it to DNA. Keep under 1,400 words.

## Phase 1: Computing from the ground up

### 1.1 Bits, gates and the digital abstraction (core, about 9 min)

Bit = a physical distinction a system can make reliably. Gates AND, OR, NOT; NAND alone suffices (universality). Substrates that have computed: relays, valves, vacuum tubes, transistors, fluidics, dominoes. Five requirements for a logic family: nonlinearity; gain (signal restoration); fan-out; cascadability (output is a valid input); isolation (outputs do not disturb inputs). Noise margins: why a gate that snaps sloppy inputs to clean outputs lets errors never accumulate. ChemE picture: a relief valve or a thermostat as a threshold device. DNA bridge: signal = high or low concentration of a strand; seesaw gate threshold plus catalytic amplification = restoration (Qian and Winfree 2011); cascadable because outputs are strands of the same form; isolation imperfect (leak, crosstalk). Self-check: why can no linear device be a logic gate; what does gain buy.

### 1.2 State, memory and time (core, about 14 min)

Combinational versus sequential logic. Feedback makes memory: a latch is a bistable system; ChemE picture: a stirred reactor with two stable steady states and hysteresis between ignition and extinction. Flip-flops, registers. The clock: global agreement on when values are valid; without it, races. Finite-state machines; counters. Asynchronous logic exists but is hard. Chemistry: a well-mixed tube has no clock; every reaction runs at once. Strategies: one-shot feed-forward circuits; separation of timescales; externally stepped protocols (add instruction strands, wait, repeat, as in SIMD DNA, Wang 2023); thermal cycling as a clock (PCR; heat-recharge, Song and Qian 2025); chemical oscillators (Srinivas 2017). Two kinds of molecular memory: concentrations (state, easily disturbed) and sequence (non-volatile, the storage tier).

### 1.4 The stored-program machine and the memory hierarchy (core, about 13 min)

Von Neumann machine: memory holds data and instructions alike; processor fetches, decodes, executes. Memory hierarchy with rough access times: register under a nanosecond; cache a few nanoseconds; RAM about 100 nanoseconds; flash about 100 microseconds; disk about 10 milliseconds; tape seconds to minutes; DNA storage hours to days. Capacity and cost per bit run the other way. The von Neumann bottleneck: moving data between memory and processor dominates time and energy; for AI every weight is fetched on every pass, so memory bandwidth sets speed. Responses: caches, GPUs with fast memory, in-memory computing (preview of 2.4). DNA: densest and slowest tier; demonstrated density about 215 petabytes per gram (Erlich and Zielinski 2017), theoretical ceiling far higher. Keung lab premise: compute where the data already is. ChemE picture: hold-up tanks and transfer lines; a plant limited by pumping, not by reactors.

### 1.5 What can be computed, and at what cost (core, about 8 min)

Algorithm = finite recipe. Turing machine in a picture: a tape, a head, a rule table; a polymerase walking a template is the molecular cousin. Universality: one machine can simulate any other, so a new substrate never computes anything new; it only changes speed, cost, density, energy. Complexity: how steps grow with input size; polynomial versus exponential; P, NP (easy to check), NP-complete. Adleman 1994: seven-city Hamiltonian path solved by generating all paths as DNA and filtering; about a week of bench work. Why it could not scale: candidates grow exponentially; Hartmanis's estimate that around 200 cities would need more DNA than the mass of the Earth. Lesson: parallelism buys a huge constant factor (ten to the eighteenth strands) but not an exponent. Where parallelism does win: wide, shallow work. Depth versus width; a matrix times a vector is millions of independent multiplies plus sums that can be done in a number of stages that grows only as the logarithm of the width. Amdahl's law: the serial fraction sets the limit. Carry forward: sequential depth is the scarce thing for a slow substrate.

### 1.7 Abstraction: building with billions of parts (core, about 13 min)

How digital engineering scales: layers with contracts (transistor, gate, block, processor, operating system, language). Each layer hides the one below. Made possible by restoration and standard interfaces. Design automation: describe behaviour, synthesise to gates, place and route, verify by simulation; design rules guarantee yield. ChemE picture: unit operations and P&IDs; you design a plant from characterised units, not from molecules. Molecular analog: domain level (toeholds, branch-migration domains) above sequence level; compilers (the seesaw compiler, Thubagere 2017; Peppercorn and Nuskell; Visual DSD); sequence design with NUPACK. What is missing: a characterised parts library with reliable kinetics; a design-rule checker for sequence space, because crosstalk grows with the number of sequences in the tube (this is the job BINND-like predictors do); cheap pure strands. The abstraction leaks; fixing leaks is research.

### 1.8 Information, noise and error correction (core, about 15 min)

Information as reduction of uncertainty; the bit; entropy as average surprise (fair coin one bit, loaded coin less). Channel capacity: a noisy channel still carries a definite maximum rate with arbitrarily few errors. Redundancy and codes: repetition, parity, Hamming, Reed-Solomon for bursts and erasures, fountain codes (any sufficient subset of packets recovers the file; DNA Fountain 2017, CHECKED citation). The DNA channel: substitutions, insertions, deletions, whole strands lost, uneven copy numbers; inner and outer codes; sequencing depth as a cost. Analog side: bits carried by one analog value = log base two of the number of distinguishable levels; a signal-to-noise power ratio of one hundred gives about 3.3 bits; a concentration known to plus or minus five percent gives about ten levels, a little over three bits. That number returns in lesson 2.2.

### 1.9 Reliable computing from unreliable parts (core, about 14 min)

Von Neumann 1956: reliable machines from unreliable parts by redundancy plus restoring organs (majority vote); a threshold: below a per-gate error rate, arbitrarily long computation is possible at some overhead. Modern forms: error-correcting memory, checksums. Biology: kinetic proofreading (Hopfield 1974, Ninio 1975) spends energy to check twice; equilibrium binding alone would give about one error in a hundred, the ribosome achieves about one in ten thousand; DNA replication with proofreading and repair about one in a billion or better. The triangle of speed, accuracy and energy. DNA circuits: errors are leak (output without input), crosstalk, synthesis truncations, pipetting. Remedies: thresholds (seesaw), clamps, leakless designs that require several unlikely events at once (Wang et al. 2018), purification. Per-layer error sets the depth you can reach before restoration.

### 1.11 Search, hashing and nearest neighbours (depth, about 12 min)

Linear search, binary search on sorted data, hash tables (address computed from content), content-addressable memory. Nearest-neighbour search in many dimensions is hard; approximate methods such as locality-sensitive hashing; vector databases and retrieval in modern AI. DNA: hybridisation is a physical lookup by content across ten to the fifteenth molecules at once; PCR primers as keys; learned encodings that make similar items bind (Bee 2021); the price is reaction time and specificity, which is what BINND predicts.

## Phase 2: Analog, digital and the physics of computation

### 2.1 Computing by analogy (core, about 14 min)

Analog computer = a physical system that obeys the same equations as the problem. Slide rule; Kelvin's tide predictor; Bush's differential analyzer (1931); electronic analog computers with op-amp integrators, summers and multipliers wired on a patch panel. ChemE heritage: process simulation and PID control ran on analog machines in the 1950s and 60s. Programming one: one integrator per state variable, then scale the variables in magnitude and in time to fit the machine's range. Strengths: all variables evolve at once, in continuous time. Weaknesses: three to four digits at best, drift, set-up labour, limited dynamic range. Then the turn: a chemical reaction network is an analog computer. Concentrations are the state variables, mass-action kinetics does the integration, programming means choosing reactions and rate constants; Soloveichik 2010 showed any such network can in principle be compiled to DNA. Magnitude and time scaling reappear as concentration ranges and rate constants.

### 2.2 The precision bill (core, about 8 min)

Every analog value carries noise. Precision in bits = log two of range over noise. Thermal-noise-limited analog: one more bit means halving the noise relative to signal, which costs four times the power or energy: cost grows as four to the number of bits. Digital: one more bit is one more wire and a little more logic: cost grows about linearly (quadratically for multiplication). Crossover: analog wins below roughly six to eight bits, digital above (Sarpeshkar 1998). Error accumulation: analog errors compound stage by stage; digital gates restore. Chemistry's noise budget: counting noise goes as one over root N; at one nanomolar in ten microlitres there are about six billion molecules, so counting noise is negligible; in a femtolitre (a bacterium) one nanomolar is less than one molecule, so it dominates. In bulk tubes the errors are systematic: pipetting at one to five percent, strand purity, rate constants, leak. So a bulk DNA signal is good to three to five bits. Hybrid answer: compute in analog for a few stages, then restore. Preview: inference needs four to eight bits, training more.

### 2.4 The analog comeback: why AI reopened the question (core, about 7 min)

Why analog came back: Dennard scaling ended in the mid-2000s; AI is dominated by matrix-times-vector; most energy goes on moving weights. In-memory analog computing: weights stored as conductances at the crossings of a grid of wires; Ohm's law multiplies, Kirchhoff's current law adds; a whole matrix-vector product in one step, where the data sit. Devices: resistive memory, phase-change memory, flash. What goes wrong: device variability, drift, few distinguishable levels (roughly four to six bits), wire resistance, and converters at the edges that take most of the energy and area. Hardware-aware training: inject the hardware's noise during training. Inference works; training on the device is hard because it needs tiny, symmetric, repeatable updates. Also photonics and spiking neuromorphic chips, in a sentence each. DNA bridge: the same structure (concentrations as weights, mass action multiplies, mixing adds) with the same failings and the same remedies.

### 2.5 Mortal computation: machines that learn in their own physics (core, about 8 min)

Hinton's argument (2022 paper, 2023 lectures): digital computing is immortal because software is separable from hardware, which requires identical, precise, power-hungry components. Give that up and each device can be cheap, low-power, even grown, with learning working around its quirks. Price: knowledge dies with the device; transfer only by teaching (distillation); and backpropagation needs an exact model of the forward pass, which you no longer have. Hence interest in forward-forward, perturbation methods, equilibrium propagation, and hybrid physics-aware training (Wright 2022: forward pass in the real system, backward pass in a digital model; CHECKED: optics, mechanics, electronics). The sim-to-real gap. DNA bridge: every tube is a slightly different computer; and DNA is half immortal: sequences can be copied exactly (PCR), concentrations cannot. Which knowledge you put in sequence and which in concentration is a design choice.

### 2.7 What a bit costs: the thermodynamics of computation (core, about 9 min)

Landauer: erasing one bit costs at least k T ln 2, about 3 times ten to the minus 21 joules at room temperature. Bennett: logic itself can be reversible; a computer driven gently dissipates less the slower it runs; his Brownian computer and RNA polymerase as an example (order of tens of k T per base). Scale: a modern transistor switching event is of order ten thousand k T; a GPU spends roughly ten to the minus 12 joules per arithmetic operation, around a hundred million k T; a synaptic event in the brain roughly ten to the minus 14 joules. A strand displacement step releases of order ten to twenty k T. The catch: a bulk gate at 100 nanomolar in 20 microlitres involves about ten to the twelfth molecules, so one logical operation costs about ten to the minus 7 joules, far worse than a GPU. DNA wins on energy only when each molecule does distinct work (search across stored data) or volumes shrink. Also: the energy was paid at synthesis. Speed-accuracy-energy trade (kinetic proofreading). Two 2025-26 results: heat as a universal recharge (Song and Qian 2025, CHECKED) and computing by relaxing to equilibrium (Stérin et al. 2026, CHECKED: ten programs, 25-bit addition, reusable dozens of times, small instances under a minute).

### 2.9 Where analog meets digital: converters and hybrid machines (core, about 12 min)

Converters: digital-to-analog on the way in, analog-to-digital on the way out; each extra bit of resolution roughly doubles to quadruples converter cost; in analog AI chips converters dominate. Design rule: cross the boundary as rarely as possible and restore when you do. For a tube: writing = synthesis (slow, costly per base) or dispensing premade strands (a liquid handler is a converter good to a few percent); reading = fluorescence (seconds, a few channels), sequencing (counts molecules; hours; billions of reads), nanopores (streaming). The clock = whatever steps the protocol: a robot, a thermal cycler, a pump. Consequences: few, fat steps; read rarely; keep state in molecules between steps. Use order-of-magnitude figures only and say they move fast.

### 2.10 A scorecard for any computing substrate (core, about 10 min)

KEYSTONE. Thirteen questions: signal carrier; primitive operations; gain and restoration; fan-out; wiring and addressing; time per operation; energy per operation; density; error per operation; parallelism; cost and delay of input and output; programmability and reuse; cost to make. Apply to five systems with rough numbers. Silicon logic: tens of picoseconds per gate, about ten to the minus 16 joules per switch, essentially error-free, wires as lithographed metal. Brain: milliseconds, about 20 watts in total, ten to the fourteenth or more synapses. Analog in-memory chips: one step per matrix-vector product, four to six bits. Well-mixed strand displacement: seconds to minutes per reaction at best, hours for multilayer circuits; wires are sequences; a few hundred distinct species demonstrated; one-shot until 2025; three to five bits. DNA storage: about 215 petabytes per gram demonstrated, read latency hours, write cost the bottleneck, lifetimes of thousands of years cold. End: which rows are physics and which are engineering not yet done.

## Phase 3: How AI models are built, trained and run

### 3.1 From random forests to deep learning (core, about 12 min)

Supervised learning as he knows it: features, label, loss, train and test. Trees and boosting: superb on tables, weak on raw images and sequences because they have no notion of locality or composition. Deep learning: learn the features too, by stacking differentiable layers trained end to end with gradient descent; needs data and compute; architecture carries assumptions (convolution: local patterns anywhere; attention: content-based interaction). Rule of thumb: a 500-row assay table wants boosting; 144.6 million raw sequence pairs want a network. Vocabulary map: model, parameters, weights, loss, epoch, batch, optimiser, hyperparameter, validation set.

### 3.2 A network is a stack of matrix multiplications (core, about 13 min)

Neuron = weighted sum plus bias, then a nonlinearity. Layer = matrix times vector plus bias. Without nonlinearity a stack collapses to one linear map. ReLU. Forward pass. Counting parameters: inputs times outputs plus outputs; BINND has 4,467,969 (CHECKED). Cost: one multiply-add per weight per example. Batches turn it into matrix times matrix. Outputs: logits to probabilities by sigmoid or softmax; cross-entropy loss as surprise. Width versus depth. What hardware must do: multiply-accumulate at scale and apply a simple nonlinearity.

### 3.4 Backpropagation out loud (core, about 17 min)

KEYSTONE. Goal: how much would the loss change if each weight changed a little. Naive: nudge each weight and rerun, millions of passes. Backpropagation: one backward sweep. Blame assignment through the chain rule; computational graph; the forward pass stores every activation; the backward pass carries an error signal layer by layer, using each layer's stored input and the same weights transposed. Cost about two to three forward passes; memory = all activations. Update: weight minus learning rate times gradient. Four demands on hardware: the backward path must know the forward weights exactly (weight transport); per-example activations must be stored; error signals are signed and span a wide range; updates are tiny and must accumulate faithfully over millions of steps. This list is why inference in chemistry is far easier than training in chemistry.

### 3.5 Making training work (core, about 15 min)

Minibatch stochastic gradient descent and why noise helps; epochs; learning rate as the main knob; schedules and warm-up; momentum; Adam; initialisation; batch and layer normalisation; residual connections; regularisation by weight decay, dropout, early stopping; reading training against validation loss. BINND (CHECKED): ReLU, batch normalisation and dropout after each convolution; early stopping with patience of two epochs; hyperparameters searched with Ray Tune and the ASHA scheduler, which stops unpromising trials early.

### 3.7 Convolutions: pattern detectors that slide (core, about 12 min)

A filter is a small weight pattern slid along the input; shared weights mean few parameters and the same detector everywhere. For DNA: one-hot input four rows by L columns; a filter eight wide is a learned motif detector, a cousin of a position weight matrix. Stacking builds grammar from motifs; pooling; receptive field; channels; then fully connected layers. BINND (CHECKED): the two 20-mers are interleaved into a 4 by 40 matrix so each base sits beside its would-be partner; a small filter then sees a candidate base pair and its neighbours, which is where stacking energy lives. Encoding as prior knowledge. A RoBERTa-style transformer gained about 0.1 percent for 13.5 times the training time.

### 3.9 Sequences: from recurrence to attention (core, about 16 min)

Recurrent networks: a hidden state updated token by token; sequential, forgetful; LSTM gates. Attention: every position scores every other by content (query against key) and takes a weighted mix of values: a soft, differentiable lookup by content. Transformer block = attention, a small feed-forward network, residual connections, normalisation; positions encoded separately. Parallel across positions, so GPUs suit it; cost grows with the square of length. Tokens and embeddings. Bridge: hybridisation is a hard lookup by content; attention is its soft arithmetic cousin.

### 3.11 Foundation models, embeddings and in-context learning (core, about 14 min)

Pretraining by prediction on unlabelled data; fine-tuning; frozen embeddings plus a small head; transfer when labels are scarce. In-context learning: behaviour changes with examples in the prompt, no weight change. Retrieval. Scaling laws in one sentence. DNA and protein language models: what they are trained on and good at; caveat that short synthetic oligos under assay conditions are far from genomes, so a small network on the right data can win, as BINND found.

### 3.14 The compute behind AI (core, about 17 min)

KEYSTONE. Count arithmetic: a forward pass is about two operations per parameter per token; training about three times that. A model of 100 billion parameters trained on ten to the thirteenth tokens: order of ten to the twenty-fifth operations. A top accelerator: about ten to the fifteenth operations per second at roughly a kilowatt, so about ten to the minus 12 joules per operation; clusters of tens to hundreds of thousands. Number formats: 32-bit and 16-bit floating point, 8-bit integers. Memory bandwidth as the bottleneck. Parallel across examples and across positions; serial across layers and across update steps: a training run is on the order of a million sequential updates. The workload profile for any new hardware: dominated by multiply-accumulate; wide but with irreducible depth; millions of sequential updates; heavy memory traffic.

### 3.15 How much precision does learning need? (core, about 14 min)

Floating point in a sentence. Inference: 8-bit integers routine; 4 bits common for language models; binary or ternary weights possible at some cost (BinaryConnect, binarised networks 2015-16). Why: redundancy, averaging over many weights, training for robustness. Training needs more: each update is a tiny fraction of a weight, so low-precision weights swallow it; fixes: keep a hidden high-precision copy, or stochastic rounding (Gupta 2015: 16-bit training). Noise as regulariser; noise-aware training makes networks tolerate analog hardware. Bridge: inference at three to five bits fits a tube; for training, a concentration is a naturally fine-grained accumulator but is hard to set and read precisely.

### 3.17 Learning without backpropagation (core, about 17 min)

KEYSTONE. Nine routes. Train in software and deploy (all DNA networks before 2025). Hybrid physics-aware training. Local rules: Hebbian; delta or perceptron rule. Energy-based: Hopfield, Boltzmann machines (compare clamped and free statistics), equilibrium propagation. Forward-forward. Feedback alignment. Perturbation and evolution strategies: only forward evaluations, trivially parallel, and molecules can be copied with variation and selected, so a tube can evaluate ten to the twelfth variants. Reservoir computing: fixed dynamics, train only the read-out. Memory-based: store examples and compare (nearest centroid); Cherry and Qian 2025 is of this kind: examples written additively into concentrations (CHECKED: three sets of 100-bit patterns). For each: what it demands physically and whether chemistry has done it.

### 3.22 Generative models in brief: autoencoders and diffusion (depth, about 12 min)

Depth. Autoencoders (compress, reconstruct), variational versions, diffusion (learn to remove noise step by step), autoregressive generation; how each is used to propose sequences; evaluation pitfalls. About 1,500 words.

### 3.23 Reinforcement learning and evolution as optimisers (depth, about 12 min)

Depth. Reinforcement learning in outline (policy, reward, exploration); evolution strategies and genetic algorithms; why population methods need only forward evaluations; directed evolution and SELEX as the wet-lab versions. About 1,500 words.

## Phase 4: Building models like BINND, with Claude

### 4.2 BINND dissected: a design review (core, about 18 min)

KEYSTONE. All CHECKED against the paper. Task: do two 20-base strands bind in a pulldown. Data: 26 biotinylated bait 20-mers (pairwise Hamming distance at least 10) against a prey library; capture on streptavidin beads; NovaSeq; 28 conditions in triplicate; balanced set of about 144.6 million unique pairs; binary labels. Encoding: one-hot 4 by 40, the two strands interleaved so complementary positions are adjacent. Model: five convolutional and three fully connected layers, ReLU, batch normalisation, dropout; 4,467,969 parameters; BINND-Lite 1,092,225; PyTorch 2.6. Training: stratified random 8:1:1 split; Ray Tune with ASHA; early stopping, patience two; L40S GPUs. Results on about 14.5 million test pairs: 83 percent accuracy, area under the ROC curve 0.88; at threshold 0.5 it is conservative (few false positives, about 73 percent of true binders found). Baselines: NUPACK 0.73, Primer3 0.79, Levenshtein 0.74; a network trained on simulated free energies 66 percent. Speed: 54 times NUPACK, 7 times Primer3 on a GPU. Generalisation: training on few baits gives 0.55, about eleven baits 0.8; salt robust. Transformer: plus 0.1 percent at 13.5 times the training time. Use: a 26 by 96 bait-prey network of storybook characters, verified by pulldown. Limits: 20 bases only, binary label, one assay, random split (3-mer Jaccard check), 26 baits. Close with questions to ask of any such paper and five extensions.

### 4.3 The project workflow, and ten ways it silently goes wrong (core, about 16 min)

Workflow: decision the model serves; metric; baseline (simple and physical); look at the data; design the split; smallest end-to-end model; overfit one batch; scale; regularise; tune; test once; ablate; analyse errors; log seeds and configs. Ten silent failures with the check for each: leakage between train and test; labels misaligned after shuffling or joins; evaluating in training mode; mismatched loss and output activation; class imbalance hiding behind accuracy; preprocessing fitted on all data; tuning on the test set; an input bug that makes the model learn the base rate; conclusions from one seed; batch or condition confounded with label.

### 4.5 PyTorch by ear: the anatomy of a training script (core, about 14 min)

Tensor; Dataset and DataLoader; a module with layers and a forward method; device; loss (binary cross-entropy on logits); optimiser; the loop: zero gradients, forward, loss, backward, step; train and eval modes; no-grad evaluation; checkpoints; seeds; typical files (data, model, train, evaluate, config). Read a twenty-line loop aloud in plain English.

### 4.6 Sequence-to-function models for nucleic acids (core, about 15 min)

Questions asked of sequences: binding, rate, structure, yield, device function. Physics baselines: nearest-neighbour thermodynamics, NUPACK, Primer3; good at equilibrium duplexes, blind to kinetics, surfaces, assay artefacts. Learned models: encodings (one-hot, k-mer, interleaved pair, pairing matrix); two-tower models (fast, give embeddings for search) versus joint models (more accurate); outputs; hybrids that learn the residual of a physics model. Data sources. Examples: hybridisation kinetics (Zhang 2018), simulated-label hybridisation (Buterez 2021, CHECKED: over 2.5 million pairs), learned encodings for similarity search (Bee 2021), toehold switches (2020), BINND (2026). Uses: screening, optimisation, orthogonal sets, deliberately cross-reactive sets.

### 4.8 Directing Claude to build a model (core, about 15 min)

What Claude does well and where it fails quietly (plausible evaluation code that leaks, silently changed preprocessing, invented APIs, over-engineering). Practice: a one-page spec (decision, data schema, metric, baseline, split rule, compute budget); ask for a plan; smallest end-to-end version; insist on tests: shapes, overfit one batch, shuffled labels fall to chance, baseline comparison; ask for an adversarial review in a fresh session; read every diff that touches data; keep a results log; have it explain the training loop back. What stays yours: the split, what counts as generalisation, when to stop. Clusters and environments in two sentences.

### 4.9 Desk lab 1: a first training loop (core, about 75 min)

Lab. PyTorch, synthetic two-class data, a two-layer network. Tasks: train; plot loss; overfit one batch of 16; then learning rate too high, labels shuffled, evaluation in training mode; write one line on what each looked like.

### 4.10 Desk lab 2: a mini-BINND on simulated labels (core, about 120 min)

Lab. 200,000 random 20-mer pairs; label by a duplex free-energy calculation (primer3-py or ViennaRNA with DNA parameters) thresholded to bound or unbound, balanced; one-hot with BINND's interleaving; small 1-D convolutional network; compare with Hamming-distance and raw free-energy baselines by ROC curve.

### 4.11 Desk lab 3: evaluate like a reviewer (core, about 120 min)

Lab. Re-split so test sequences are dissimilar from training ones (cluster by k-mer profile or hold out sequence families); measure k-mer Jaccard overlap; confusion matrix across thresholds; calibration; ablate interleaved against concatenated encoding over five seeds.

### 4.12 Desk lab 4: tune and shrink (core, about 90 min)

Lab. Optuna or Ray Tune with ASHA over learning rate, dropout, filters and width; early stopping; then a model a quarter of the size; plot accuracy against parameters and against CPU inference time.

### 4.13 Desk lab 5: the real thing (core, about 120 min)

Lab. Clone github.com/dna-storage/BINND (MIT licence); build its environment; run the released model on a 26 by 96 matrix of sequence pairs; reproduce one evaluation figure on a subset of the public dataset; list any discrepancies. Runs on NC State cluster GPUs or a laptop CPU with BINND-Lite.

### 4.14 From model to design: optimisation, active learning and the wet-lab loop (depth, about 12 min)

Depth. Predictor inside a design loop: screening, genetic algorithms, gradient ascent on relaxed inputs; optimisers find a model's blind spots, so use ensembles and validate; active learning and Bayesian optimisation; automation closes the loop. About 1,500 words.

### 4.15 Desk lab 6: a neural network made of reactions (depth, about 150 min)

Lab, depth. Write mass-action equations for a three-class winner-take-all network (weighted sum, pairwise annihilation, read-out); integrate with SciPy; set weights from averaged patterns; then rewrite the integrator in PyTorch and fit the concentrations by gradient descent through the simulation: physics-aware training for chemistry.

## Phase 5: Molecular computing: the field

### 5.1 The field in one sitting (core, about 15 min)

Timeline: Seeman 1982; Adleman 1994; Winfree's tile assembly 1998; Yurke's tweezers 2000; Rothemund's origami 2006; Seelig's enzyme-free logic 2006; kinetics and reaction-network theory 2009-10; seesaw circuits and the first DNA neural network 2011; compilers, leakless design, oscillator 2017; storage track: 2012-13 first megabyte-scale demonstrations, random access 2018, similarity search 2021, computation on stored data 2023, the NC State engine 2024; neural track: winner-take-all 2018, enzymatic networks 2022, nucleation 2024, learning, heat recharge and CALCUL 2025, equilibrium computer and BINND 2026. Schools in a sentence each. Scoreboard: hundreds of distinct species; hours per run; reuse measured in tens of cycles; learning just begun.

### 5.2 Strand displacement, the transistor of DNA computing (core, about 15 min)

Domains; toehold (four to eight bases) and branch-migration domain; mechanism; rate constant rises about tenfold per toehold base then saturates near a few million per molar per second, spanning about six orders (Zhang and Winfree 2009). Driving force. Toehold exchange for reversibility; catalysis for gain; leak at roughly one to ten per molar per second as the noise floor. Why it is like a transistor and how it is not: consumed, slow, concentration-dependent. Time arithmetic: half-time = 0.69 over (rate constant times concentration): at a million per molar per second and 100 nanomolar, about seven seconds; at one nanomolar, about twelve minutes.

### 5.4 Chemistry as a programming language (core, about 15 min)

Reaction network = species, reactions, rate constants. Two semantics: deterministic equations at high counts, stochastic at low. Three computing styles: analog steady state; rate-independent computation, whose answers do not depend on rates and which computes exactly the continuous piecewise-linear functions (so minimum, maximum and ReLU are natural); stochastic networks, universal with small error. DNA as universal substrate (2010): each formal reaction becomes a few displacement steps with fuel; cost in strands; accuracy limits. Built examples: consensus (Chen 2013), oscillator (Srinivas 2017). A chemical engineer's advantage: steady states, stability, residence times.

### 5.6 Digital circuits in a test tube, and the scaling wall (core, about 15 min)

Seesaw gate: threshold soaks up input until exhausted; catalysis with fuel amplifies to full output: restoration. Dual-rail logic. Square-root circuit, 130 strands, hours (Qian and Winfree 2011). Six walls: leak grows with gate count; finite orthogonal sequence space; concentration per species falls as species rise, so speed falls; strand quality and cost; single use; hard to observe. Routes round each: leakless design, localisation, enzymes, compartments, heat recharge, learned predictors of cross-binding (BINND).

### 5.8 DNA neural networks I: how a tube computes a weighted sum (core, about 15 min)

Inputs as strands; weights as concentrations of weight molecules; sum is free because converted strands are identical; nonlinearity by threshold and amplification; negative weights need dual rail or annihilation. 2011: four neurons (Qian, Winfree, Bruck). 2018 winner-take-all (CHECKED): weighted sums per class, pairwise annihilation until one remains, restoration reports it; up to nine classes; each pattern 20 molecules chosen from 100 representing a ten by ten image; correct with up to 30 of 100 bits flipped. In machine-learning terms: a single layer, nearest-template classifier with weights computed in software by averaging.

### 5.10 DNA neural networks II: analog accuracy, reuse and learning in the tube (core, about 16 min)

Three 2025 advances, each CHECKED. Learning: Cherry and Qian, training examples as molecules, written into concentrations, then used to classify three sets of 100-bit patterns; additive, not error-driven. Reuse: Song and Qian, heat ramp re-arms more than 200 species within minutes, at least 16 rounds. Analog accuracy: CALCUL (Liu et al.), weights as concentration ratios, weighted sums accurate to a few percent, negative weights by annihilation, ReLU by a bead purification step taking hours, networks under 30 parameters, reset shown for two rounds. Plus theory: rate-independent ReLU networks (Vasić 2020). Where it stands and the next three milestones.

### 5.15 Beyond the well-mixed tube: enzymes, surfaces, compartments and cells (core, about 16 min)

Why well-mixed is the least scalable architecture. Enzymes (polymerase-nickase-exonuclease toolbox; transcriptional genelets): sustained dynamics and sharp thresholds; Okumura 2022 (CHECKED: majority on ten bits, two-layer network, cell-sized droplets). Localisation on origami (Chatterjee 2017): neighbours react fast, sequences reused. Compartments: droplets, gels, the dendricolloid: many small computers, lower molecule counts, noise returns. Cells: analog gene circuits (Daniel 2013), perceptrons in bacteria (Rizik 2022), protein winner-take-all in mammalian cells (Chen 2024). Biology keeps tens of thousands of species apart with recognition, location and proofreading, not base pairing alone.

### 5.17 Self-assembly as computation: tiles, nucleation and equilibrium (core, about 13 min)

Tile assembly as computation (Winfree 1998); Woods 2019: one tile set, many six-bit algorithms. Nucleation as classifier (Evans 2024, CHECKED): 917 tiles, three structures, 18 images of 30 by 30 pixels, trained in silico, 150-hour anneal. Equilibrium computing (Stérin 2026, CHECKED). Common thread with Hopfield networks: the program is an energy landscape.

### 5.20 DNA storage as a computer's memory (core, about 17 min)

KEYSTONE. Pipeline: encode, index, add redundancy, synthesise a pool, store, access, sequence, decode. Density about 215 petabytes per gram shown. NC State line (CHECKED for the 2024 paper): files on 50-micrometre cellulose-acetate dendricolloid particles; non-destructive reading by transcription from separate promoters; erase and replace; projected half-lives about 6,000 years at 4 Celsius and 2 million years at minus 18; RNA read by nanopore; enzymatic computation on simplified 3 by 3 chess and sudoku problems. Computing on stored data three ways: similarity search (Bee 2021: 1.6 million images, learned image-to-sequence encoding, probes as queries); parallel programs on registers (Wang 2023: data in nicks, binary counting and Rule 110, 4-bit registers, 244 strand exchanges); and designed cross-binding networks (BINND 2026). Architecture view: DNA as a memory tier with associative search built in.

### 5.55 Tools of the trade: simulators, compilers and sequence design (depth, about 12 min)

Depth. NUPACK, ViennaRNA, Primer3 (thermodynamics); Visual DSD, Peppercorn, Nuskell (enumeration and compilation); Multistrand, oxDNA (kinetics and coarse-grained dynamics); plain ODE solvers. What each answers. About 1,400 words.

### 5.56 Who's who: labs, meetings and how to read the field (depth, about 10 min)

Depth. Labs and what each is known for; the DNA computing conference, FNANO, SEED; molpigs; how to read a paper in ten minutes with the three questions. About 1,200 words.

## Phase 6: Toward AI in DNA

### 6.1 Sizing the problem (core, about 17 min)

KEYSTONE. Currencies: operations, memory, precision, sequential depth, distinct addresses, time, energy, money. What chemistry offers: a micromole is six times ten to the seventeenth molecules; a bimolecular step takes one over (rate constant times concentration); three to five bits per concentration; few distinct interacting species; cheap events but many copies. The dilution law: total concentration is capped, so concentration per species falls as species are added and every reaction slows in proportion. A well-mixed analog matrix with a million weights would need a million species at picomolar each, hours per step. The alternative: sequence as data, one instruction applied to all molecules. Throughput arithmetic: ten to the fifteenth molecules stepped once an hour is far below one accelerator; but enzymes turn over hundreds of times a second each, so raw molecular throughput can be astronomical. Conclusion: throughput is not the bottleneck; organisation is: addressing, precision, depth, and getting data in and out. Five places DNA could win.

### 6.2 The design space: seven routes to molecular AI (core, about 20 min)

KEYSTONE. Seven routes, each with what is shown, what binds, the tenfold levers. A: train in software, run in chemistry. B: hybrid training with the tube in the loop. C: learning rules in chemistry. D: storage-centred associative computing. E: evolution and selection as learning. F: equilibrium and energy-landscape computing. G: spatial, compartmentalised and enzymatic hardware underneath all the others. The general idea that molecular parallelism favours wide, shallow computation, stated as a hypothesis with its addressing problem. The hybrid machine: electronic controller, molecular co-processor.

### 6.4 The interface and the clock (core, about 13 min)

Budget for input and output: synthesis (cost per base, days), enzymatic synthesis, premade libraries assembled combinatorially, epigenetic writing (2024: 350 bits per reaction); dispensing; reading by fluorescence, sequencing, nanopore. The clock: stepped protocols, thermal cycling, microfluidics; cycle times of minutes. Design consequences: few fat steps, sparse read-out, state kept in molecules, the robot as part of the computer. A cost model: dollars per cycle plus dollars per molecule-operation.

### 6.5 Open problems, and how to choose yours (core, about 17 min)

KEYSTONE. Ten open problems with what a result looks like: cross-binding prediction at scale; reusable clocked circuits for hundreds of cycles; error-driven learning in vitro; automated hybrid training loops; AI primitives inside storage; calibrated analog sums to five or six bits; a compiler from a trained network to strands with cost estimates; benchmarks and metrics; addressable compartment arrays; equilibrium computing for sampling and optimisation. Choosing: importance, tractability, your edge (kinetics, transport, reactor thinking, scale-up, automation, process economics); prefer problems where a negative result teaches; build the measurement first; set kill criteria.

### 6.6 Capstone at the desk: a two-page architecture memo (core, about 180 min)

Capstone. Two pages: one architecture from lesson 6.2, the workload it targets, a resource estimate using the scorecard, the first experiment, three kill criteria. Then a fresh Claude session reviews it as a sceptical computer architect.

### 6.8 What would change my mind: milestones and kill criteria (depth, about 12 min)

Depth. Setting numerical milestones and kill criteria in advance; examples for three of the ten problems. About 1,400 words.
