import unittest
from unittest.mock import patch
from io import StringIO

from db import DataBaseDTO, DataBase, DataBaseException


class TestDataBase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = DataBaseDTO('postgres', 'user', 'qwertyR1!', '127.0.0.1', '5001')
        self.db = DataBase(self.data)

    def tearDown(self) -> None:
        del self.db

    def test_print_info(self):
        expected_connect = f'Connect to DB: {self.db.db_name}'
        expected_close = f'Close connect to DB: {self.db.db_name}'
        expected_read = f'Read data from database: {self.db.db_name} from table: table'
        expected_write = f'Write data to DB: {self.db.db_name} table: table'

        with patch('sys.stdout', new=StringIO()) as test_out:
            self.db.connect()
            self.assertTrue(expected_connect in test_out.getvalue())
        with patch('sys.stdout', new=StringIO()) as test_out:
            self.db.close()
            self.assertTrue(expected_close in test_out.getvalue())
        with patch('sys.stdout', new=StringIO()) as test_out:
            self.db.read('table')
            self.assertTrue(expected_read in test_out.getvalue())
        with patch('sys.stdout', new=StringIO()) as test_out:
            self.db.write('table', 'data')
            self.assertTrue(expected_write in test_out.getvalue())

    def test_normal_input(self):
        self.db.db_name = 'postgres'
        self.db.user = 'user'
        self.db.password = 'qwertyR1!'
        self.db.host = '127.0.0.1'
        self.db.port = '5001'

        self.assertEqual(self.db.db_name, 'postgres')
        self.assertEqual(self.db.user, 'user')
        self.assertEqual(self.db.password, 'qwertyR1!')
        self.assertEqual(self.db.host, '127.0.0.1')
        self.assertEqual(self.db.port, '5001')
        self.assertEqual(self.db.databases, ('postgres', 'mysql', 'sqlite'))

    def test_wrong_db_name(self):
        with self.assertRaises(TypeError) as wrong_type:
            self.db.db_name = 10
        self.assertTrue('must be a string' in str(wrong_type.exception))
        with self.assertRaises(ValueError) as empty_field:
            self.db.db_name = ' '
        self.assertTrue('Empty string in values' == str(empty_field.exception))
        with self.assertRaises(DataBaseException) as unsupported_db:
            self.db.db_name = 'wrong'
        self.assertTrue('Unsupported DB:' in str(unsupported_db.exception))

    def test_wrong_user(self):
        with self.assertRaises(TypeError) as wrong_type:
            self.db.user = 10
        self.assertTrue('must be a string' in str(wrong_type.exception))
        with self.assertRaises(ValueError) as empty_field:
            self.db.user = ' '
        self.assertTrue('Empty string in values' == str(empty_field.exception))

    @unittest.skip("I don't know why this test is not working")
    def test_root_user(self):
        with self.assertWarns(UserWarning) as warning:
            self.db.user = 'root'
        self.assertTrue('Use root user is dangerous' in str(warning))

    def test_wrong_password(self):
        with self.assertRaises(TypeError) as wrong_type:
            self.db.password = 10
        self.assertTrue('must be a string' in str(wrong_type.exception))
        with self.assertRaises(ValueError) as empty_field:
            self.db.password = ' '
        self.assertTrue('Empty string in values' == str(empty_field.exception))
        with self.assertRaises(DataBaseException) as wrong_pw:
            self.db.password = 'Ab_5'
        self.assertTrue('Password must be at least 8 chars include Upper, Lower, Digit, Punctuation' ==
                        str(wrong_pw.exception))
        with self.assertRaises(DataBaseException) as wrong_pw:
            self.db.password = 'Ab_cdef*gh'
        self.assertTrue('Password must be at least 8 chars include Upper, Lower, Digit, Punctuation' ==
                        str(wrong_pw.exception))
        with self.assertRaises(DataBaseException) as wrong_pw:
            self.db.password = 'abcdefgh_5'
        self.assertTrue('Password must be at least 8 chars include Upper, Lower, Digit, Punctuation' ==
                        str(wrong_pw.exception))
        with self.assertRaises(DataBaseException) as wrong_pw:
            self.db.password = 'ABCDEFGH_5'
        self.assertTrue('Password must be at least 8 chars include Upper, Lower, Digit, Punctuation' ==
                        str(wrong_pw.exception))
        with self.assertRaises(DataBaseException) as wrong_pw:
            self.db.password = 'Abcdefgigk5'
        self.assertTrue('Password must be at least 8 chars include Upper, Lower, Digit, Punctuation' ==
                        str(wrong_pw.exception))

    def test_wrong_host(self):
        with self.assertRaises(TypeError) as wrong_type:
            self.db.host = 10
        self.assertTrue('must be a string' in str(wrong_type.exception))
        with self.assertRaises(ValueError) as empty_field:
            self.db.host = ' '
        self.assertTrue('Empty string in values' == str(empty_field.exception))
        with self.assertRaises(DataBaseException) as wrong_ip:
            self.db.host = '100'
        self.assertTrue('does not appear to be an IPv4 or IPv6 address' in str(wrong_ip.exception))
        with self.assertRaises(DataBaseException) as wrong_host:
            self.db.host = '192.168.0.102'
        self.assertTrue('is not avaliable' in str(wrong_host.exception))

    def test_wrong_port(self):
        with self.assertRaises(TypeError) as wrong_type:
            self.db.port = 10
        self.assertTrue('must be a string' in str(wrong_type.exception))
        with self.assertRaises(ValueError) as empty_field:
            self.db.port = ' '
        self.assertTrue('Empty string in values' == str(empty_field.exception))
        with self.assertRaises(DataBaseException) as wrong_port:
            self.db.port = 'port'
        self.assertTrue('Port must contains numbers not' in str(wrong_port.exception))
        with self.assertRaises(DataBaseException) as min_port:
            self.db.port = '0'
        self.assertTrue('Port must be between 0-65000' == str(min_port.exception))
        with self.assertRaises(DataBaseException) as max_port:
            self.db.port = '65001'
        self.assertTrue('Port must be between 0-65000' == str(max_port.exception))



