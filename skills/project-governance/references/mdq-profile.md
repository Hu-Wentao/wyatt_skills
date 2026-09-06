---
mdq:
  version: 1
  records:
    boundary: {levels: [1], pattern: '^Shared MDQ Profile$'}
    key: {source: marker}
  fields:
    title: {source: heading}
    raw: {source: body}
  tolerance: {incomplete: true}
---
<!-- mdq:record id="GOV-SHARED-MDQ-PROFILE" -->
# Shared MDQ Profiles

Use the smallest versioned shared profile that matches the document family.
Profiles are complete declarations: a consuming document supplies only the
profile reference, not a second inline extraction contract.

| Family | Reference | Shape and standard named queries |
| --- | --- | --- |
| Generic governed records | `project-governance/governed-document-v1` | Level-2 structured IDs and standard governance labels; no named query requirement |
| Defects | `project-governance/defect-profile-v1` | `DEF-YYYYMMDD-slug` level-1 records; `defect_by_id` |
| Domain definitions | `project-governance/domain-profile-v2` | `DD-*` level-2 records; `definition_by_id`, status, and context queries |
| Marketing leads | `project-governance/marketing-profile-v2` | `MKT-LEAD-####` level-2 records; lead identity and facet queries |
| Technical evaluations | `project-governance/evaluation-profile-v1` | `TECH-EVAL-*` level-1 records |
| Technical fit evaluations | `project-governance/evaluation-profile-v2` | `TECH-FIT-*` level-1 records; `fit_by_id` |

The family version in the reference is independent of the mdq protocol version
inside the asset. For example, `defect-profile-v1` is a first published family
contract and uses mdq v2 because it owns a reusable named query.

## Profile Identity

- Reference: `project-governance/governed-document-v1`
- Asset: `assets/mdq-profiles/governed-document-v1.yaml`
- Profile version: `1`
- mdq protocol version: `1`

Reference it from YAML Front Matter instead of copying the complete extraction
contract into every document:

```yaml
---
mdq:
  profile: project-governance/governed-document-v1
---
```

A reference is the complete `mdq` declaration. Do not combine it with inline
`version`, `records`, `fields`, tolerance, query, maintenance, or index keys.
Use a normal inline contract when the document has a different boundary, key
scheme, field vocabulary, or query requirement. Do not force an old archive or
one-off record into a family merely to remove YAML. `README.md` remains
ordinary and must not reference a profile.

## Resolution and Safety

`queryable-markdown` resolves the namespace only to the sibling skill asset at
`<skills-root>/project-governance/assets/mdq-profiles/`. A document cannot
supply a filesystem path, URL, import, command, or plugin. Missing, malformed,
ambiguous, unversioned, or metadata-mismatched references are invalid and must
not fall back to temporary selectors for a write.

The resolved profile participates in the normal profile hash. A profile change
therefore invalidates an older derived index. Document mutations may update
only authored record bytes; the mdq optimizer must not rewrite a shared profile
through one consuming document.

## Version Policy

Treat `governed-document-v1` as immutable after publication. Any change to
record identity, boundaries, field extraction, tolerance, or compatibility
semantics creates a new asset and reference such as `governed-document-v2`.
Keep the old asset while documents still reference it. The filename suffix,
`x-profile-id`, `x-profile-version`, and mdq `version` must agree.

The same immutability rule applies to every family in the catalog. Add a new
family version when its boundary, key pattern, field vocabulary, query names,
query quality limits, or maintenance policy changes. A profile may use mdq v2
while retaining a family version such as `v1`; the two version values have
different meanings and must not be conflated.

Changing a document from one profile version to another is a contract migration,
not an incidental content edit. Inspect the document first, compare exact keys
and representative fields before and after the migration, then run:

```bash
uv run <queryable-markdown-root>/scripts/mdq.py check <document.md> \
  --tier contract
```

Preserve existing inline contracts unless migration is explicitly authorized.
