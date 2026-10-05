# Evidence policy

A useful portfolio should make its claims inspectable and bounded.

| Claim type | Evidence required |
| --- | --- |
| Implemented behavior | Relevant source inspected at a recorded revision |
| Passing tests | An executed run or a matching CI report, with its scope stated |
| Deployed software | Deployment evidence, distinguished from independent live-user acceptance |
| Business improvement | A measurement with a baseline, time period, and attribution limits |
| Production integration | Actual integration code and execution evidence; names or interfaces alone are insufficient |
| Security or scientific validation | The relevant independent evaluation; source controls and passing tests are not substitutes |

Implementation observed in source is described as implemented or present in the reviewed source. Prototype behavior is labeled. Proposed metrics, future work, and product directions are not reported as achieved outcomes.

Commercial source and private reports remain private. Their observations are summarized at a level suitable for explaining product and engineering decisions. Public reviewers can inspect this documentation and its checker; they cannot independently inspect every private claim from this repository alone.

[Dated verification notes](verification.md) · [Portfolio](../README.md)
