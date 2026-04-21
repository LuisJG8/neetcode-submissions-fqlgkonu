class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        em = set()

        for x in emails:
            local, root = x.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            em.add((local, root))
        return len(em)