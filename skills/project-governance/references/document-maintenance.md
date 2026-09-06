---
mdq:
  version: 1
  dialect: gfm
  records:
    boundary:
      source: heading
      levels: [1]
      pattern: '^Document Maintenance$'
    key:
      source: marker
  fields:
    title:
      source: heading
    raw:
      source: body
  tolerance:
    incomplete: true
---
<!-- mdq:record id="GOV-DOCUMENT-MAINTENANCE" -->
# Document Maintenance

Maintain the complete project documentation surface without confusing
inventory, structural repair, and semantic lifecycle decisions. Use a
risk-based path: keep exact low-risk edits small, and reserve project-wide
maintenance gates for changes that can alter authority or lifecycle meaning.

## Separate Inventory from Governance

Inventory every project-owned Markdown document when the selected scope is
`all-markdown`. Exclude Git metadata, dependencies, generated build output,
runtime caches, and vendored trees. Inventory does not make every Markdown file
a governed document and does not require every README, package guide, or
operations note to adopt an `mdq` contract.

Treat `README.md` as a user-facing introduction, not as a governance record or
internal lifecycle index. Exclude README files from the governed-document set;
do not add a persistent `mdq` contract to them. Put internal collection indexes
in `INDEX.md` or another dedicated governed document.

Require persistent `mdq` contracts only for project-governed requirements,
baselines, plans, dependency evaluations, defects, archives, coverage,
verification, and traceability documents. Preserve repository-owned governed
roots when they differ from the defaults. For compatible level-2 heading
records, use the versioned shared contract in [mdq-profile.md](mdq-profile.md)
instead of copying the same selector and field block into every document.
Profile-free ordinary Markdown queries remain read-only and must not acquire a
contract merely because they were inspected. The `queryable-markdown` semantic
CLI may recall likely records for review, but its index is a local derived
cache; revalidate each candidate with deterministic mdq before governance or
write decisions.

Also govern repository-embedded architecture and API contract artifacts even
when their owning runtime convention places them outside `docs/`. The managed
profile recognizes `*.bff.md` throughout the project while excluding Git
metadata, dependencies, generated output, caches, and vendored trees. Treat
this suffix as an explicit contract convention, not as a reason to govern
ordinary Markdown beside source code. Embedded contracts participate in the
same persistent-mdq, source-snapshot, plan, and verify gates as docs-owned
records.

## Choose the Smallest Path

Do not require every document change to run every maintenance operation.
Classify the requested mutation by its observable risk, not only by the number
of files involved.

### Fast path: one low-risk exact-record edit

Use the queryable-markdown fast path when all of the following are true:

- the target document has a valid persistent contract;
- one exact, case-sensitive record is already known;
- the edit does not change identity, boundaries, contract metadata, lifecycle
  status, links, indexes, or another document;
- the replacement value is supplied by the request and does not need semantic
  invention.

Use `get` or `set` to retrieve and preflight the target, apply the smallest
source patch or scalar transaction, and run the smallest sufficient `mdq check`
tier. A project-wide `inspect`, `plan`, or `maintain` operation is not required
for this path.

### Full path: semantic or cross-document maintenance

Use the full path for new documents, contract or identity changes, lifecycle
status, requirements, baselines, plans, archives, indexes, links, or any
cross-document change:

1. Run `inspect` when the scope, authority, or current source is not already
   known.
2. Run `plan` when semantic decisions, multiple plausible repairs, or
   cross-document effects need to be recorded.
3. Use `maintain` with current explicit write authorization as the bounded
   preflight for the selected scope. It does not itself replace the
   queryable-markdown edit.
4. Apply the approved edits through `queryable-markdown` transactions.
5. Run `verify` for the authorized scope.

`maintain` is therefore a full-path authorization and source-snapshot gate,
not a mandatory ceremony for every single-record edit.

Keep operation mutability in the task contract. Do not use a runtime parameter
to turn one read-only operation into a write operation.

## Classify Repairs

Treat these as mechanical only when the authoritative source and exact repair
are unambiguous:

- a missing or invalid persistent contract whose existing record boundary,
  stable identity, and authored fields are already explicit;
- a lifecycle field that exists in authored content but is not exposed by the
  contract;
- a broken local link with one exact moved target;
- an omitted lifecycle-index entry whose document and authored state agree;
- stale derived indexes or caches.

Require semantic review for:

- requirement, plan, evaluation, or defect status;
- whether implementation and acceptance evidence complete a plan;
- baseline extraction, supersession, rejection, or archival;
- conflicting identities, duplicate authority, or competing link targets;
- authored content that must be invented rather than exposed.

Do not infer semantic completion from directory placement, document age,
passing tests, a commit message, or a lifecycle index. `mdq` exposes authored
state; it does not decide that state.

## Apply Safely

Before each write, confirm that the selected document still matches the
inspected source. Partition concurrent work only across disjoint files. Apply
shared requirement indexes, baseline indexes, plan indexes, and cross-document
reference repairs serially after the disjoint edits converge.

For every governed document edit:

1. resolve the exact record identity and source range;
2. preserve authored bytes outside the authorized record or contract control
   region;
3. apply the smallest profile reference, contract, field, status, link, or
   lifecycle change;
4. choose the smallest sufficient verification evidence:
   - `mdq check --tier content` for an existing prose or field value;
   - `mdq check --tier structure` for identity, heading, marker, label, ordering,
     or boundary changes;
   - `mdq check --tier contract` for contract, query, or index-policy changes;
   - collection `verify` after full-path or cross-document maintenance.

Stop with `decision_required` when evidence is insufficient or multiple
semantic repairs remain plausible. A maintenance request authorizes only its
selected documentation scope; it does not authorize code changes, releases,
deployment, publication, or external writes.

## Preserve Compatibility

Treat `docs audit` as a backward-compatible read-only audit operation with its
legacy output schema. Use `docs verify` for expanded lifecycle verification.
Prefer the queryable-markdown fast path for one low-risk exact-record edit and
the `document-maintenance` task for the full path. Keep the legacy
`document-audit` task resolvable while configured projects migrate their
contracts. Existing `maintain` operations remain compatible, but are not
required when the fast-path conditions hold.
