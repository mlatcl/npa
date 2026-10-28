"""Map 2006 notes chapters and FoilTeX heads onto LaMD lecture files."""

from __future__ import annotations

import re

# lecture id -> (week, session, title, featured_image, date, abstract)
LECTURES = {
    "course-info-practical": {
        "kind": "practical",
        "week": 1,
        "session": 0,
        "title": "Course information (2006–07)",
        "date": "2006-09-25",
        "featured_image": "",
        "abstract": (
            "Front matter of the 2006--07 lecture notes: rooms, calendar, "
            "evaluation, reading list, and how the notes sit against Bertsekas "
            "and Gallager."
        ),
    },
    "introduction-and-networks": {
        "kind": "lecture",
        "week": 1,
        "session": 1,
        "title": "Introduction and Networks",
        "date": "2006-09-25",
        "featured_image": "slides/diagrams/npa/1975_net_map.png",
        "abstract": (
            "Background to telecommunication networks, from Morse and Erlang to "
            "ARPANET and the internet, and the vocabulary of circuit switching, "
            "packet switching, and sessions that the rest of the course uses."
        ),
    },
    "probability-review": {
        "kind": "lecture",
        "week": 1,
        "session": 2,
        "title": "Probability Review",
        "date": "2006-09-25",
        "featured_image": "slides/diagrams/npa/pdfOfHeight.png",
        "abstract": (
            "Joint, marginal, and conditional probability, the sum and product "
            "rules, expectations, the Poisson distribution, densities and CDFs, "
            "and sample averages."
        ),
    },
    "poisson-processes": {
        "kind": "lecture",
        "week": 1,
        "session": 3,
        "title": "Poisson Processes",
        "date": "2006-09-26",
        "featured_image": "slides/diagrams/npa/sumPoisson.png",
        "abstract": (
            "The Poisson process as a counting process, superposition and "
            "decomposition, independence on disjoint intervals, and exponential "
            "interarrival times including the memoryless property."
        ),
    },
    "birth-death-mm1": {
        "kind": "lecture",
        "week": 2,
        "session": 1,
        "title": "Birth-Death Processes and the M/M/1 Queue",
        "date": "2006-10-02",
        "featured_image": "slides/diagrams/npa/stateMM1.png",
        "abstract": (
            "Markov chains and the Markov property, Coin Monopoly as a route "
            "from a binomial walk to the Poisson process, birth-death balance, "
            "Kendall's notation, and the geometric occupancy of M/M/1."
        ),
    },
    "littles-formula": {
        "kind": "lecture",
        "week": 2,
        "session": 2,
        "title": "Little's Formula",
        "date": "2006-10-03",
        "featured_image": "slides/diagrams/npa/littlesFormula.png",
        "abstract": (
            "Time averages versus distribution means, Little's formula "
            r"$\bar{N}=\lambda\bar{T}$ for $G/G/1$ in steady state, and its use "
            r"on $M/M/1$ to split sojourn time into waiting and transmission."
        ),
    },
    "other-markov-queues": {
        "kind": "lecture",
        "week": 4,
        "session": 1,
        "title": "Other Markov Queues",
        "date": "2006-10-16",
        "featured_image": "slides/diagrams/npa/stateMM1m.png",
        "abstract": (
            r"Finite buffer $M/M/1/m$ and the infinite-server $M/M/\infty$ queue, "
            "with blocking probability and the Poisson occupancy."
        ),
    },
    "erlang-delay": {
        "kind": "lecture",
        "week": 4,
        "session": 2,
        "title": "Erlang Delay",
        "date": "2006-10-16",
        "featured_image": "slides/diagrams/npa/erlangDelay.png",
        "abstract": (
            r"The $M/M/m$ delay system, Erlang C, waiting probability, and mean "
            "occupancy."
        ),
    },
    "erlang-loss": {
        "kind": "lecture",
        "week": 5,
        "session": 1,
        "title": "Erlang Loss",
        "date": "2006-10-23",
        "featured_image": "slides/diagrams/npa/erlangLossFlowChart.png",
        "abstract": (
            r"The $M/M/m/m$ loss system, truncated Poisson occupancy, Erlang B, "
            "and carried load."
        ),
    },
    "mg1": {
        "kind": "lecture",
        "week": 6,
        "session": 1,
        "title": "The M/G/1 Queue",
        "date": "2006-10-30",
        "featured_image": "slides/diagrams/npa/residualTime.png",
        "abstract": (
            "Residual service time and the Pollaczek--Khinchin formula, the "
            r"$M/M/1$ and $M/D/1$ special cases, and $M/G/1$ with vacations."
        ),
    },
    "mg1-arq": {
        "kind": "lecture",
        "week": 6,
        "session": 2,
        "title": "M/G/1 and Automatic Repeat Request",
        "date": "2006-10-31",
        "featured_image": "slides/diagrams/npa/ARQ.png",
        "abstract": (
            "Stop-and-wait ARQ as an $M/G/1$ service time: geometric "
            "retransmissions, utilisation, and the second moment."
        ),
    },
    "networks-of-queues": {
        "kind": "lecture",
        "week": 7,
        "session": 1,
        "title": "Networks of Queues and Jackson's Theorem",
        "date": "2006-11-06",
        "featured_image": "slides/diagrams/npa/kleinrockNetwork.png",
        "abstract": (
            r"Tandem $M/M/1$, time reversibility and Burke's theorem, Kleinrock's "
            "independence assumption, Jackson's theorem, and ns-2 as the lab "
            "counterpart."
        ),
    },
    "aloha": {
        "kind": "lecture",
        "week": 8,
        "session": 2,
        "title": "Multiaccess and ALOHA",
        "date": "2006-11-14",
        "featured_image": "slides/diagrams/npa/pureALOHA.png",
        "abstract": (
            "Statistical multiplexing versus TDMA/FDMA, pure ALOHA with a "
            "vulnerable period of two packet times, slotted ALOHA, and the "
            "backlog delay."
        ),
    },
}

# Chapter title (normalised) -> lecture id. Order matters for prefix matches.
CHAPTER_TO_LECTURE = [
    ("schedule", "course-info-practical"),
    ("introduction and background", "introduction-and-networks"),
    ("network performance analysis", "introduction-and-networks"),
    ("probability review", "probability-review"),
    ("poisson processes", "poisson-processes"),
    ("markov chains and markov processes", "birth-death-mm1"),
    ("birth death processes", "birth-death-mm1"),
    ("littles formula", "littles-formula"),
    ("other markov queues", "other-markov-queues"),
    ("erlang delay", "erlang-delay"),
    ("erlang loss", "erlang-loss"),
    ("automatic repeat request", "mg1-arq"),
    ("m/g/1", "mg1"),
    ("networks of queues", "networks-of-queues"),
    ("multiaccess", "aloha"),
]

# Foil index ranges (1-based, inclusive) from lectureSlides.lyx.
FOIL_RANGES = [
    (1, 4, "course-info-practical"),
    (5, 16, "introduction-and-networks"),
    (17, 40, "probability-review"),
    (41, 51, "poisson-processes"),
    (52, 93, "birth-death-mm1"),
    (94, 114, "littles-formula"),
    (115, 122, "other-markov-queues"),
    (123, 137, "erlang-delay"),
    (138, 146, "erlang-loss"),
    (147, 177, "mg1"),
    (178, 189, "mg1-arq"),
    (190, 212, "networks-of-queues"),
    (213, 243, "aloha"),
]


def normalise_title(title: str) -> str:
    title = title.replace("'", "").replace("’", "")
    title = re.sub(r"\\label\{[^}]*\}", " ", title)
    title = title.replace("$", " ")
    title = re.sub(r"\\[A-Za-z]+", " ", title)
    title = re.sub(r"[^A-Za-z0-9/]+", " ", title)
    title = re.sub(r"\s*/\s*", "/", title)
    return re.sub(r"\s+", " ", title).strip().lower()


def lecture_for_chapter(title: str) -> str | None:
    norm = normalise_title(title)
    for prefix, lecture_id in CHAPTER_TO_LECTURE:
        if prefix in norm:
            return lecture_id
    return None


def lecture_for_foil(index: int) -> str | None:
    for start, end, lecture_id in FOIL_RANGES:
        if start <= index <= end:
            return lecture_id
    return None
