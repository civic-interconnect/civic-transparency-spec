# Privacy

The Civic Transparency framework is designed with **privacy by design** at its core.

## Guiding Principles

1. **No personal data.**  
   The system does not collect or expose account IDs, handles, user names, or message text.

2. **Bucketed fields.**  
   Potentially sensitive attributes (e.g., account age, follower count) are reported only in broad, non-identifying ranges.

3. **Aggregate-only outputs.**  
   All metrics are computed across large groups; no individual-level records are exposed.

4. **Minimum group size thresholds.**  
   Public outputs are only generated when `k-anonymity ≥ 100` is satisfied, reducing re-identification risk.

5. **No cross-platform joins.**  
   Schema design avoids linkable identifiers across platforms, making external joining infeasible.

## Built-in Safeguards

- **Small-count suppression.**  
  Metrics for small groups are suppressed to prevent triangulation attacks.

- **Raw-post decoupling.**  
  Public outputs are derived from aggregate computations, not individual post logs.

- **Internal-only provenance tags.**  
  Tags are used to compute trends and coordination patterns, but never exposed at the individual post level.

## Legal & Ethical Compliance

- **Privacy-aligned.**  
  Meets the intent of privacy regulations such as the **GDPR**, **CCPA**, and other global standards.

- **Transparency-compliant.**  
  Enables platforms to meet obligations under emerging transparency laws (e.g., the **EU Digital Services Act**) without revealing personally identifiable information.

---

_This privacy approach is central to building trust while enabling visibility into coordinated behavior online._
