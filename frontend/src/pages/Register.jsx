import Container from "../components/shared/Container"
import AuthCard from "../components/shared/AuthCard"
import { Helmet } from "react-helmet"

const Register = () => {
    return (
        <>
            <Helmet>
                <title>Register</title>
            </Helmet>
            <Container>
                <div className="hidden lg:flex lg:items-center lg:justify-center lg:w-1/2">
                    <div className="w-1/2 mx-auto">
                        <h1 className="text-indigo-300 font-bold text-6xl">Network</h1>
                        <p className="text-slate-50 text-2xl leading-normal">Share your voice, spread kindness, make an impact, let the Network amplify your spirit!</p>
                    </div>
                </div>
                <AuthCard>
                    <form className="flex flex-col items-center justify-center space-y-4 mb-2">
                        <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="text" placeholder="Fullname" />
                        <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="email" placeholder="Email" />
                        <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="text" placeholder="Username" />
                        <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="password" placeholder="Password" />
                        <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="password" placeholder="Confirm Password" />
                        <input className="block w-full bg-indigo-400 rounded-lg p-2 text-white text-lg font-medium hover:cursor-pointer" type="submit" value="Sign up" />
                    </form>
                    <p className="text-sm text-slate-500">Already have an account?</p>
                    <a className="block text-sm text-indigo-400 hover:text-indigo-500 hover:underline hover:decoration-indigo-500" href="#">Log in</a>
                </AuthCard>
            </Container>
        </>

    )
}

export default Register