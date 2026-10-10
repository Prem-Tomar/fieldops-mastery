# Problem statement

A maintenance company dispatches technicians to customer sites. Dispatchers schedule on web; technicians accept work, record notes/photos, and consume parts on mobile. Organizations cannot see one another's jobs. Connectivity is unreliable, operations repeat, and staff disagree.

## Initial vertical slice

Create job → assign technician → accept/start on mobile → record work and parts → complete → view accepted completion on web.

Start with synthetic fixtures and one organization, then add another. Roles: dispatcher, technician, organization administrator.

## Business guarantees

- State transitions follow an explicit domain policy.
- Stock cannot become negative; repeated completion cannot deduct it twice.
- Local acknowledgement means durable local intent; server acknowledgement means accepted server state.
- Offline acknowledged edits survive termination.
- Tenant/resource authorization covers reads, writes, files, and subscriptions.
- Conflicts preserve history and evidence.
- Failed operations remain visible and recoverable.
- Supported old clients remain compatible.
- Reconnected clients recover authoritative state.

## Questions to resolve before implementation

What counts as overlapping work? Can completion survive cancellation? What can an offline user view after revocation? How long are idempotency records retained? Which fields merge safely? How is replay-history expiration handled?

Document alternatives and review product-policy choices before encoding them. Do not hide ambiguity behind silent overwrite.

Payments, AI, video calls, sophisticated routing, and extensive analytics are future scope. Reports and scheduling simulations are bounded backend exercises.
