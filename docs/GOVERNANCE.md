# Repository governance

Authorized merger: **Prem-Tomar**, user ID **6422761**. Default branch: **master**.
Collaborators work on branches/forks and submit PRs. No invitations until usernames are supplied.

## Enforcement

Two branch rulesets target refs/heads/master:

1. Restrict updates, bypassed only by Prem-Tomar through pull requests.
2. No bypass: require PRs, resolved conversations, linear history, passing curriculum-validation; block deletion and force pushes.

The owner exception does not waive quality checks or allow direct pushes. Admins can edit rules, so grant no additional administration or bypass actors.

Squash is the only merge method. Auto-merge is disabled. CODEOWNERS requests the owner's review but does not itself restrict merges. Required approval count is zero to avoid a sole-owner self-review deadlock; reciprocal review and owner review are procedural, while update restrictions enforce the merger identity.

## Visibility and verification

GitHub rejected rulesets on the initial private repository with HTTP 403 requiring Pro or public visibility. The owner explicitly authorized public visibility.

The stored JSON files describe intended settings; only live GitHub rules enforce them. Verify active rules, bypass IDs, branch, and merge settings after applying.

## References

- [Rulesets and plan availability](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).
- [Available rules and restricted updates](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets).
- [Rules API and bypass semantics](https://docs.github.com/en/rest/repos/rules).
