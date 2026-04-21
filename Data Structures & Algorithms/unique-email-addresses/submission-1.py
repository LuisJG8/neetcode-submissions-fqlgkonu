class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        em = set()

        for x in emails:
            local, root = x.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            em.add((local, root))
        return len(em)

        # method 2
        em = set()

        for e in emails:
            i, local = 0, ""
            while e[i] not in ["@", "+"]:
                if e[i] != ".":
                    local += e[i]
                i += 1
            
            while e[i] != "@":
                i += 1
            domain = e[i + 1:]
            unique.add((local, domain))

        return len(em)