<img src="assets/header.svg" alt="Amirhossein Akhoondzadeh, senior mobile engineer. Lead AI agents. Ship mobile software you can trust." width="100%">

<p align="center">
  <a href="https://www.youtube.com/@essentialsemicolon"><img src="assets/btn-youtube.svg" alt="essential semicolon on YouTube" height="44"></a>
  <a href="https://www.linkedin.com/in/amirhosseinakhoondzadeh"><img src="assets/btn-linkedin.svg" alt="LinkedIn" height="44"></a>
  <a href="mailto:amirhossein.akhoondzadeh@gmail.com"><img src="assets/btn-email.svg" alt="Email" height="44"></a>
</p>

<p align="center">
  <img src="assets/stack.svg" alt="Flutter, Dart, Android, iOS, architecture, testing, AI-assisted workflows" width="100%">
</p>

## The channel

essential semicolon is for working mobile engineers who hand real work to
AI coding agents and still have to sign off on what ships. Each video runs
an agent on a real Flutter app, catches what it got right or wrong on
screen, teaches the concept behind it, and shows what the run cost.

A win gets reported as a win. The first five repos below hold the code
from an episode, so you can clone one and check the claim yourself.

## What is in here

**[trip-wallet](https://github.com/amirhosseinakhoondzadeh/trip-wallet)**
is the repo behind the spec sections episode. A Flutter trip expense app,
written for the demo by an AI coding agent, where an agent was asked to
add the trip total in the home currency. It holds the full spec, four
copies with one section cut, the one sentence version, the wrapper text,
and three of the 30 runs as branches, each exactly as the agent left it.

**[flutter-parallel-shop](https://github.com/amirhosseinakhoondzadeh/flutter-parallel-shop)**
is the repo behind the parallel agents episode. Two Claude Code agents
worked on two branches of a Flutter shop, both passed their own tests, and
git merged them with zero conflicts. The merged code failed
`flutter analyze` with four errors. It holds both branches as the agents
left them, the merge, the two prompts and the held back price test.

**[flutter-spec-vs-prompt](https://github.com/amirhosseinakhoondzadeh/flutter-spec-vs-prompt)**
is the repo behind the spec versus prompt episode. The same model built
one Flutter feature twice: once from a one sentence request, once from a
`SPEC.md` and six acceptance tests written before the code. After a new
persistence requirement, the six tests were untouched and still passed.

**[flutter-search-race-repro](https://github.com/amirhosseinakhoondzadeh/flutter-search-race-repro)**
is the repo behind the channel's pumpAndSettle video. A Flutter search
screen with a deliberately planted race, where an older `b` request
lands after a newer `ba` one and overwrites it. It holds the agent's
test run, the `pumpAndSettle` comparison that stops waiting 400 ms
before the stale response arrives, a fake-clock timeline printed every
100 ms, the spinner that times out, and the three-line guard that fixes
it. Every command in its README is verified from a fresh clone.

**[flutter-textfield-loses-text-repro](https://github.com/amirhosseinakhoondzadeh/flutter-textfield-loses-text-repro)**
is the repo behind the channel's TextField video. A 48 line Flutter app
where one tap makes a TextField forget everything you typed: the bug, an
instrumented field that prints when its State is born and dies, two
fixes on two branches, and a six variant widget test that proves in
about two seconds which half of the fix does the work.

**[weather_app_flutter](https://github.com/amirhosseinakhoondzadeh/weather_app_flutter)**
is the architecture showcase. Clean Architecture split across data, domain and
presentation, Bloc for state, get_it for injection, and 13 tests over the
bloc, the local datasource and both use cases. It reads from OpenWeatherMap
and handles nested vertical and horizontal scrolling, which is the part
that usually breaks.

**[energy_monitor_app_flutter](https://github.com/amirhosseinakhoondzadeh/energy_monitor_app_flutter)**
is the same architecture pointed at a local JSON API. fl_chart draws the
solar, house and battery series, and the watts to kilowatts switch
re-renders from data already fetched rather than calling the API again.
29 tests, including a widget test over the whole page.

**[mason_flutter_meetup_berlin_23](https://github.com/amirhosseinakhoondzadeh/mason_flutter_meetup_berlin_23)**
is the sample project from a talk I gave at a Flutter meetup in Berlin in
April 2023. It carries `meetup_brick`, a Mason brick that generates a full
Clean Architecture feature folder from two prompts.

**[flutter_design_patterns](https://github.com/amirhosseinakhoondzadeh/flutter_design_patterns)**
is the decorator pattern in Dart, written as a menu where each topping
wraps the item under it.
