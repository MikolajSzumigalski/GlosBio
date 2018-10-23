import unittest
import shutil

from .SampleManager import SampleManager, UsernameException


class TestSampleManager(unittest.TestCase):

    def setUp(self):
        self.sample_manager = SampleManager('./test')
        self.username = "qwe rty"

    def tearDown(self):
        shutil.rmtree('./test', ignore_errors=True)

    def test_username_to_dirname_should_pass(self):
        username = 'Abcd Efgh'
        dirname = self.sample_manager.username_to_dirname(username)
        self.assertEqual(dirname, 'abcd_efgh')

    def test_username_to_dirname_invalid_username(self):
        username = 'a ?'
        with self.assertRaises(UsernameException) as ctx:
            self.sample_manager.username_to_dirname(username)
        self.assertIn('Incorrect username "a_?" !', str(ctx.exception))

    def test_create_user_should_pass(self):
        self.sample_manager.create_user(self.username)

    def test_create_users_should_pass(self):
        uname1 = "asd asd"
        uname2 = "dasd dasd"
        self.sample_manager.create_user(uname1)
        self.sample_manager.create_user(uname1)
        self.sample_manager.create_user(uname2)

    def test_user_exists(self):
        no = self.sample_manager.user_exists(self.username)
        self.assertFalse(no)
        self.sample_manager.create_user(self.username)
        yes = self.sample_manager.user_exists(self.username)
        self.assertTrue(yes)

    def test_get_all_usernames(self):
        uname1 = "Aud asd"
        uname2 = "śćą ÜüŹąłä"
        unames = [uname1, uname2, self.username]
        for uname in unames:
            self.sample_manager.create_user(uname)
        dirnames = set(['aud_asd', 'sca_uuzala', 'qwe_rty'])
        self.assertEqual(dirnames, set(self.sample_manager.get_all_usernames()))

    def test_add_sample_without_user_should_not_pass(self):
        sample = b'aaaaaaaa'
        with self.assertRaises(FileNotFoundError):
            self.sample_manager.add_sample(self.username, sample)

    def test_add_sample_should_pass(self):
        sample = b'aaaaaa'
        self.sample_manager.create_user(self.username)
        self.sample_manager.add_sample(self.username, sample)

    def test_get_samples(self):
        self.sample_manager.create_user(self.username)
        self.assertEqual([], self.sample_manager.get_samples(self.username))
        samples = [b'asdasd', b'bbbbb', b'cccc']
        for sample in samples:
            self.sample_manager.add_sample(self.username, sample)
        self.assertEqual(
            ['1.wav', '2.wav', '3.wav'],
            self.sample_manager.get_samples(self.username)
        )

    def test_get_sample_should_pass(self):
        pass

    def test_get_json_path(self):
        example_path_wav = "C:/a.wav"
        example_path_webm = "/home/train/5.webm"

        suggested_json_path_wav = self.sample_manager.get_new_json_path(
            audio_path=example_path_wav)
        self.assertEquals(suggested_json_path_wav, "C:/a.json")

        suggested_json_path_wav = self.sample_manager.get_new_json_path(
            audio_path=example_path_webm)
        self.assertEquals(suggested_json_path_wav, "/home/train/5.json")
        



if __name__ == '__main__':
    unittest.main()
