from win32com import client


class EFTServer:
    def __init__(self, eft_server, eft_port, eft_user, eft_password):
        self.eft_server = eft_server
        self.eft_port = eft_port
        self.eft_user = eft_user
        self.eft_password = eft_password
        self.rule_list = []
        self.user_list = []
        self.site_list = []

    def get_rules(self):

        eft = client.Dispatch("SFTPComInterface.CIServer")

        eft.ConnectEx(self.eft_server, self.eft_port, 0, self.eft_user, self.eft_password)
        sites = eft.Sites()
        num_of_sites = sites.Count()
        event_rule_types = eft.AvailableEvents

        for event_rule_type in event_rule_types:
            for site_number in range(1, (num_of_sites + 1)):
                site = sites.SiteByID(site_number)
                e_rules = site.EventRules(event_rule_type.type)
                for iRule in range(e_rules.count()):
                    obj_event = e_rules.Item(iRule)
                    params = obj_event.GetParams()
                    name = str(params.Name)
                    if name != "None":
                        self.rule_list.append(name)

    def disable_rule(self, rule_name):
        eft_server = self.eft_server
        eft_port = self.eft_port
        eft_user = self.eft_user
        eft_password = self.eft_password
        eft = client.Dispatch("SFTPComInterface.CIServer")

        eft.ConnectEx(eft_server, eft_port, 1, eft_user, eft_password)

        sites = eft.Sites()
        num_of_sites = sites.Count()
        event_rule_types = eft.AvailableEvents

        for event_rule_type in event_rule_types:
            for site_number in range(1, num_of_sites):
                site = sites.SiteByID(site_number)
                e_rules = site.EventRules(event_rule_type.type)
                for iRule in range(e_rules.count()):
                    obj_event = e_rules.Item(iRule)
                    params = obj_event.GetParams()
                    name = str(params.Name)
                    if name == rule_name:
                        params.Enabled = "false"
                        obj_event.SetParams(params)

    def enable_rule(self, rule_name):
        eft_server = self.eft_server
        eft_port = self.eft_port
        eft_user = self.eft_user
        eft_password = self.eft_password
        eft = client.Dispatch("SFTPComInterface.CIServer")

        eft.ConnectEx(eft_server, eft_port, 1, eft_user, eft_password)

        sites = eft.Sites()
        num_of_sites = sites.Count()
        event_rule_types = eft.AvailableEvents

        for event_rule_type in event_rule_types:
            for site_number in range(1, num_of_sites):
                site = sites.SiteByID(site_number)
                e_rules = site.EventRules(event_rule_type.type)
                for iRule in range(e_rules.count()):
                    obj_event = e_rules.Item(iRule)
                    params = obj_event.GetParams()
                    name = str(params.Name)
                    if name == rule_name:
                        params.Enabled = "true"
                        obj_event.SetParams(params)

    def get_users(self):
        eft_server = "localhost"
        eft_port = "1100"
        eft_user = "Admin123"
        eft_password = "Admin123!!!"

        eft = client.Dispatch("SFTPComInterface.CIServer")

        eft.ConnectEx(eft_server, eft_port, 0, eft_user, eft_password)

        sites = eft.Sites()
        num_of_sites = sites.Count()

        for site_number in range(1, (num_of_sites + 1)):
            site = sites.SiteByID(site_number)
            users = site.GetUsers()
            for user in users:
                self.user_list.append(user)

    def disable_user(self, username):
        eft_server = self.eft_server
        eft_port = self.eft_port
        eft_user = self.eft_user
        eft_password = self.eft_password

        eft = client.Dispatch("SFTPComInterface.CIServer")

        eft.ConnectEx(eft_server, eft_port, 0, eft_user, eft_password)

        sites = eft.Sites()
        num_of_sites = sites.Count()

        for site_number in range(1, (num_of_sites + 1)):
            site = sites.SiteByID(site_number)
            user_list = site.GetUsers()
            for user in user_list:
                if user == username:
                    site.EnableUsers(user, False)

    def enable_user(self, username):
        eft_server = self.eft_server
        eft_port = self.eft_port
        eft_user = self.eft_user
        eft_password = self.eft_password

        eft = client.Dispatch("SFTPComInterface.CIServer")

        eft.ConnectEx(eft_server, eft_port, 0, eft_user, eft_password)

        sites = eft.Sites()
        num_of_sites = sites.Count()

        for site_number in range(1, (num_of_sites + 1)):
            site = sites.SiteByID(site_number)
            user_list = site.GetUsers()
            for user in user_list:
                if user == username:
                    site.EnableUsers(user, True)

    def get_sites(self):
        eft_server = self.eft_server
        eft_port = self.eft_port
        eft_user = self.eft_user
        eft_password = self.eft_password

        eft = client.Dispatch("SFTPComInterface.CIServer")

        eft.ConnectEx(eft_server, eft_port, 0, eft_user, eft_password)

        sites = eft.Sites()
        num_of_sites = sites.Count()

        for site_number in range(1, (num_of_sites + 1)):
            site = sites.SiteByID(site_number)
            self.site_list.append(site.Name)

    def disable_site(self, site_name):
        eft_server = self.eft_server
        eft_port = self.eft_port
        eft_user = self.eft_user
        eft_password = self.eft_password

        eft = client.Dispatch("SFTPComInterface.CIServer")

        eft.ConnectEx(eft_server, eft_port, 0, eft_user, eft_password)

        sites = eft.Sites()
        num_of_sites = sites.Count()

        for site_number in range(1, (num_of_sites + 1)):
            site = sites.SiteByID(site_number)
            if site.Name == site_name:
                site.stop()

    def enable_site(self, site_name):
        eft_server = self.eft_server
        eft_port = self.eft_port
        eft_user = self.eft_user
        eft_password = self.eft_password

        eft = client.Dispatch("SFTPComInterface.CIServer")

        eft.ConnectEx(eft_server, eft_port, 0, eft_user, eft_password)

        sites = eft.Sites()
        num_of_sites = sites.Count()

        for site_number in range(1, (num_of_sites + 1)):
            site = sites.SiteByID(site_number)
            if site.Name == site_name:
                site.start()

    def disable_arm(self):
        eft_server = self.eft_server
        eft_port = self.eft_port
        eft_user = self.eft_user
        eft_password = self.eft_password

        eft = client.Dispatch("SFTPComInterface.CIServer")

        eft.ConnectEx(eft_server, eft_port, 0, eft_user, eft_password)

        eft.EnableARM = False
        eft.ApplyChanges()

    def enable_arm(self):
        eft_server = self.eft_server
        eft_port = self.eft_port
        eft_user = self.eft_user
        eft_password = self.eft_password

        eft = client.Dispatch("SFTPComInterface.CIServer")

        eft.ConnectEx(eft_server, eft_port, 0, eft_user, eft_password)

        eft.EnableARM = True
        eft.ApplyChanges()
